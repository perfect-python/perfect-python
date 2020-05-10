import png


def main():

    # 出力先ファイルオブジェクトを開く
    # バイナリーモードにしなけれないけない
    fp = open('output.png', 'wb')

    # Writer オブジェクトを作る
    # サイズは256x256でビット深度8のグレースケール（白黒）に設定する 
    w = png.Writer(256, 256, bitdepth=8, greyscale=True)

    # 0〜255までのリストを256個作成
    # 正確にはrangeオブジェクトが256個あるリスト
    # 具体的には次のようなリストが生成される（rangeオブジェクトなので実際は違う）
    # [[1, 2, 3, ..., 255],
    #  [1, 2, 3, ..., 255],
    #  [1, 2, 3, ..., 255],
    #  ...
    #  [1, 2, 3, ..., 255]]
    w.write(fp, [range(256)]*256)


if __name__ == '__main__':
    main()

