#インポート
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('edgelist.txt', nodetype=str)

plt.figure(figsize=(7, 7))

pos = nx.spring_layout(G, k=0.7)

#PageRankの追加
pr = nx.pagerank(G)

nx.draw_networkx_edges(G, pos, edge_color='y')

#node_sizeにPageRankの値を組み込む
nx.draw_networkx_nodes(
    G,
    pos,
    node_color='r',
    alpha=0.5,
    node_size=[5000*v for v in pr.values()]
)
nx.draw_networkx_labels(
    G,
    pos,
    font_size=10
)

plt.axis('off')
plt.show()

