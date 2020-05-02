import sys
import os
import imp
import http.client
from urllib import parse

EXTENTION = '.txt'

def _create_full_path(path, fullname):
    """インターネットのパスを生成するヘルパー関数。

    ※ファインダー・ローダーの本質ではありません。
    """
    url_component = parse.urlparse(path)
    target = url_component.scheme + '://' + url_component.netloc \
             + os.path.join(os.path.normpath(url_component.path), \
             *(fullname.split('.'))) + EXTENTION
    return target

def _package_path(path, fullname):
    """インターネットのパッケージパスを生成するヘルパー関数。

    ※ファインダー・ローダーの本質ではありません。
    """
    target = _create_full_path(path, fullname)
    res = os.path.dirname(target) + '/{0}/__init__'.format(fullname) + EXTENTION
    return res

def _exist_url(target):
    """指定されたパスがインターネット上に存在するか確認するヘルパー関数。

    ※ファインダー・ローダーの本質ではありません。
    """
    url_component = parse.urlparse(target)
    conn = http.client.HTTPConnection(url_component.netloc)
    conn.request("HEAD", url_component.path)
    res = conn.getresponse()
    if __debug__:
        print('{0}: {1}'.format(res.status, target))
    if 200 <= res.status < 400:
        return True
    return False

def is_package(path, fullname):
    return _exist_url(_package_path(path, fullname))


class HttpImportFinder:
    EXTENTION = '.txt'

    def __init__(self, path_entry):
        self.path_entry = path_entry
        if path_entry.index('http://') != 0:
            raise ImportError() #扱えない場合には ImportError を送出します
        return #コンストラクタは値を返せませんので、呼び出し可能オブジェクトが値を返すことは期待されません
    
    def find_module(self, fullname, path=None):
        if is_package(self.path_entry, fullname):
            #指定されたパッケージを見つけたらローダーを返します
            return HttpImportLoader(self.path_entry)
        target = _create_full_path(self.path_entry, fullname)
        if _exist_url(target):
            #指定されたモジュールを見つけたらローダーを返します
            return HttpImportLoader(self.path_entry)
        return None #パッケージ・モジュールを見つけられない場合には None を返します


class HttpImportLoader:
    def __init__(self, path):
        self.path_entry = path
    
    def load_module(self, fullname):
        if fullname in sys.modules:
            #sys.modules に同じ名前があったら、再利用しなければなりません
            mod = sys.modules[fullname]
        else :
            #モジュールをロードする前に必ず sys.modules に追加します
            mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        if is_package(self.path_entry, fullname):
            target = _package_path(self.path_entry, fullname)
            #パッケージの場合にはパスを設定します。サブモジュールはこのパスを起点にして探索・インポートされます
            mod.__path__ = [self.path_entry]
            mod.__package__ = fullname #自分自身です
        else :
            target = _create_full_path(self.path_entry, fullname)
            #モジュールの場合、自分自身のパスを設定します
            mod.__path__ = _create_full_path(self.path_entry, fullname)
            mod.__package__ = '.'.join(fullname.split('.')[:-1]) #親の名前を設定します
        mod.__file__ = target
        mod.__name__ = fullname
        mod.__loader__ = self
        code = self.get_source(fullname)
        exec(code, mod.__dict__)
        return mod
    
    def get_source(self, fullname):
        if is_package(self.path_entry, fullname):
            target = _package_path(self.path_entry, fullname)
        else :
            target = _create_full_path(self.path_entry, fullname)
        url_component = parse.urlparse(target)
        conn = http.client.HTTPConnection(url_component.netloc)
        conn.request("GET", url_component.path)
        res = conn.getresponse()
        code = res.read()
        return code
    
    def get_code(self, fullname):
        source = self.get_source(fullname)
        return compile(source, fullname, 'exec', dont_inherit=True)
    
    def is_package(self, fullname):
        return is_package(self.path_entry, fullname)
    
    def get_filename(self, fullname):
        if is_package(self.path_entry, fullname):
            return _package_path(self.path_entry, fullname)
        else:
            return _create_full_path(self.path_entry, fullname)

sys.path_hooks.append(HttpImportFinder)
sys.path.append('http://localhost/')

from mtsuyuki import samp
print(samp.hello())
