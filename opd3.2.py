import networkx as net
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
G = net.DiGraph()
data = pd.read_csv("squirrel_edges.csv")


nodes = data.apply(lambda row: (row['id1'], row['id2']), axis=1)
G.add_edges_from(nodes)
print(G)
net.draw(G)
plt.show()