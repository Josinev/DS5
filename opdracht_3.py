import numpy as np
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def create_initial_star_graph(n0):
    G = nx.Graph()
    G.add_node(0)  # Hub node
    for i in range(1, n0):
        G.add_node(i)
        G.add_edge(0, i)
    print(G)
n0 = 5  # You can change this value
initial_graph = create_initial_star_graph(n0)

