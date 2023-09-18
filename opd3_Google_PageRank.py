import networkx as net
import matplotlib.pyplot as plt
g = net.Graph()

N = 3
M = 4
n0 = 5
nodes = []
for i in range(1,N+1):
    for j in range(i+1,i+M+2):
        nodes.append((i,j))

print(nodes)
g.add_edges_from(nodes)
net.draw(g)
plt.show()