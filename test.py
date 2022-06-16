# import matplotlib.pyplot as plt
# import networkx as nx
# import random
#
# G = nx.gnp_random_graph(10,0.3)
# for u,v,d in G.edges(data=True):
#     d['weight'] = random.random()
#
# edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
# print(weights)
# pos = nx.spring_layout(G)
# nx.draw(G, pos, node_color='b', edgelist=edges, edge_color=weights, width=10.0, edge_cmap=plt.cm.Blues)
# plt.savefig('edges.png')
# plt.show()

# Python Program illustrating
# pyplot.colorbar() method
import matplotlib.pyplot as plt
import numpy as np
# creates four Axes
# fig, axes = plt.subplots(nrows=2, ncols=2)
#
# for ax in axes.flat:
#     im = ax.imshow(np.random.random((10, 10)), vmin=0, vmax=1)


x = np.linspace(0, 10, 10)
print(x)
I = np.sin(x) * np.cos(x[:, np.newaxis])
print(I)
plt.imshow(I)
plt.colorbar()
plt.show()

