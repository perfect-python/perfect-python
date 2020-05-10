import networkx as nx

def main():
    g = nx.Graph()

    nx.add_start(g, range(5))
    nx.add_start(g, range(5, 10))
    g.add_node('aaaa')
    
    # 接続されているノードごとのまとまりに分ける関数: connected_components
    print(list(nx.connected_components(g))) #=> [[0, 1, 2, 3, 4], [8, 9, 5, 6, 7], ['aaaa']]

    # ここで、'aaaa' を 1 と繋げてみる
    g.add_edge(1, 'aaaa')

    # 'aaaa' が1つ目のグループに組み込まれる
    print(list(nx.connected_components(g))) #=> [[0, 1, 2, 3, 4, 'aaaa'], [8, 9, 5, 6, 7]]


if __name__ == '__main__':
    main()