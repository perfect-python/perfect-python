import networkx as nx

g = nx.Graph()

# パスを追加する
# この場合は、g.add_edges_from([(1, 2), (2, 3), (3, 4)]) と等価
nx.add_path(g, [1, 2, 3, 4])

print(g.edges()) #=> [(1, 2), (2, 3), (3, 4)]

g = nx.Graph()

# 星構造を追加する
# リストの1つ目のnodeを中心に、それ以降の要素にそれぞれedgeを作る # この場合は、add_edges_from([(1, 2), (1, 3), (1, 4)]) と等価
g.add_start([1, 2, 3, 4])
print(g.edges()) #=> [(1, 2), (1, 3), (1, 4)]