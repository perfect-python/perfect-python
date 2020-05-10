import networkx as nx
from matplotlib import pyplot

def main():
    g = nx.star_graph(5)

    # パスを追加する
    x.add_path(g, [5, 6, 7, 8, 9, 10])
    nx.add_path(g, [5, 20, 10])

    # 3から10までの最短経路を計算する
    print(nx.shortest_path(g, 3, 10)) #=> [3, 0, 5, 20, 10]

    nx.draw(g)
    pyplot.show()


if __name__ == '__main__':
    main()