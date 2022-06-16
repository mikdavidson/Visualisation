import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import geopandas as gpd
import pandas as pd
from matplotlib import cm

for i in range(27):
    shapefile = 'WP/ZAF_adm1.shp'
    graphFile = 'GWN/Graph Files/graph_' + str(i) + '.csv'
    graph = pd.read_csv(graphFile)
    graph = graph.drop(['Unnamed: 0'], axis=1)
    G = nx.DiGraph()
    G.add_nodes_from(graph['Node'])
    pos = {}
    imageFile = 'GWN/Adj Images/gwn_adjacency_matrix_' + str(i) + '.png'
    for feature_name in ['Weight']:
        max_value = graph[feature_name].max()
        min_value = graph[feature_name].min()
        graph[feature_name] = (graph[feature_name] - min_value) / (max_value - min_value)

    for i in range(len(graph)):
        G.add_edge(graph.at[i, 'Node'], graph.at[i, 'Target'], weight=graph.at[i, 'Weight'])
        pos[graph.at[i, 'Node']] = (graph.at[i, 'Longitude'], graph.at[i, 'Latitude'])

    # creating a color list for each edge based on weight

    G_edges = G.edges()
    G_weights = [G[source][dest]['weight'] for source, dest in G_edges]

    fig, ax = plt.subplots(figsize=(8, 6))
    gdf = gpd.read_file(shapefile)
    minx, miny, maxx, maxy = gdf.total_bounds
    ax.set_xlim(17.5, 21.7)
    ax.set_ylim(-35, -31)
    gdf.plot(ax=ax)


    mcl = nx.draw_networkx_edges(
        G, pos, node_size=1, edge_cmap=cm.get_cmap('YlOrRd'), width=1,
        edge_color=[G[u][v]['weight'] for u, v in G_edges],
        arrowstyle='-|>')

    nx.draw_networkx_nodes(G, pos, node_color='#FF0000', node_size=6)
    nx.draw_networkx_labels(G, pos)
    sm = plt.cm.ScalarMappable(cmap=cm.get_cmap('YlOrRd'))
    # plt.colorbar(sm)
    cbar = plt.colorbar(sm)
    cbar.set_label('Edge Weights', rotation=270, labelpad=12)
    plt.savefig(imageFile, bbox_inches='tight')
    plt.show()
