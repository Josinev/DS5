import networkx as net
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
import numpy as np
G = net.DiGraph()
data = pd.read_csv("squirrel_edges.csv") #Data inladen 


nodes = data.apply(lambda row: (row['id1'], row['id2']), axis=1) #The creation of tuples for the first and second nodes.
G.add_edges_from(nodes) #This will add the edges to the graph
r = net.pagerank(G, alpha=0.85, personalization=None, weight='weight', dangling=None) #Standard properties

plt.bar(list(r.keys()), r.values()) #Distribution of the PageRank probabilities in a bargraph
#plt.hist(r.values()) #Distribution oft eh PageRank probabilities in a histogram
plt.show()
