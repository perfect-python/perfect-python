import png
import functools
import operator



def output_gen():
    ''' 出力用のデータ列を作る関数 '''

    result = []

    # 高さ分の繰り返し
    for y in range(256):

        # 1行分のデータの並び
        # データは次のようにr, g, b, の並びで1ピクセルを表現する
        # [r, g, b, r, g, b, ..., r, g, b]
        row = []

        # 幅の分の繰り返し
        for x in range(256):

            # R
            row.append(x)
            # G
            row.append(y)
            # B
            row.append(255-(x+y)//2)

        result.append(row)

    return result
    


def main():

    # 出力先ファイルオブジェクトを開く
    # バイナリーモードにしなけれないけない
    fp = open('output2.png', 'wb')

    # Writerオブジェクトを作る
    # サイズは256xでRGB各要素のビット数は8に設定する 
    w = png.Writer(256, 256, bitdepth=8, greyscale=False)

    # output_gen関数の返値を出力する
    w.write(fp, output_gen())



if __name__ == '__main__':
    main()
