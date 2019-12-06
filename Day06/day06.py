# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 07:50:06 2019

@author: Nino
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


fname = 'input.txt'
data = pd.read_csv(fname, delimiter=',', header=None)


def add_data_to_graph(data, plot=False):
    split_data = data[0].str.split(')', n=1, expand=True)
    G = nx.Graph()
    for i, pair in split_data.iterrows():
        G.add_edge(pair[0], pair[1])
    if plot:
        plt.subplot(121)
        nx.draw(G, node_size=20)
    return G


# add data to graph
G = add_data_to_graph(data, plot=False)

# part 1
nr_orbits = 0
for node in list(G.nodes):
    nr_orbits += nx.shortest_path_length(G, source=node, target='COM')
print(nr_orbits)

# part 2
path_length = nx.shortest_path_length(G, source='YOU', target='SAN')
print(path_length - 2)
''' minus 2 is to exclude travel from YOU to neighbour,
and from neighbour to SAN '''
