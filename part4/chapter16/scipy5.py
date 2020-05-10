import math

import numpy
from scipy import interpolate
import pylab


def main():

    # 0から2πラジアンまでの区間を9つに区切った配列を生成
    xs = numpy.linspace(0, 2*math.pi, 9)

    # その配列にsinを適用し、0から2πまでのsinを計算する
    ys = numpy.sin(xs)

    # そのままプロット
    # 詳細は Matplotlib の項へ
    pylab.plot(xs, ys, 'o-')
    pylab.show()


if __name__ == '__main__':
    main()
