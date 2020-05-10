import math

import numpy
import scipy
from scipy import interpolate
import pylab


def main():

    # 0から2πラジアンまでの区間を九つに区切った配列を生成
    xs = numpy.linspace(0, 2*math.pi, 9)

    # その配列にsinを適用し、0から2πまでのsinを計算する
    ys = numpy.sin(xs)

    # xs, ysを元にスプライン補間クラスのインスタンスを生成
    ius = interpolate.InterpolatedUnivariateSpline(xs, ys)

    # 最初に作った配列と同じ範囲を200分割した配列を作成
    xn = numpy.linspace(0, 2*math.pi, 180)

    # 補間を行う
    yn = ius(xn)

    # 補間結果と元の結果をプロット
    # 詳細は Matplotlib の項へ
    pylab.plot(xs, ys, 'o-', xn, yn)
    pylab.show()


if __name__ == '__main__':
    main()
