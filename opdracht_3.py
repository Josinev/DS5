import networkx as nx
import numpy as np

def star_graph(n0, N, M):
    '''Maakt een star graph 
    input: n0 = aantal nodes waarmee het begint, N = aantal nodes uiteindelijk, M = aantal nodes waaraan die connect
    uitput: visualiseert het netwerk'''

    #Begin network
    network = nx.star_graph(n0)

#Maakt een lijst met de basis nodes
    lijst = []
    for g in range(n0 +1):
        if g > 0:
            lijst.append(g)

#Maakt de nieuwe nodes aan
    for i in range(6,N):
        #Zorgt dat die aan nodes geconnect wordt
        for j in range(M):
            #Geeft een random keuze uit de al bestaande nodes
            random_keuze = np.random.choice(lijst)
            network.add_node(i)
            #Voegt de egde toe aan de bestaande nodes
            network.add_edges_from([(i, random_keuze)])
            #Nieuwe node toe zodat er ook weer uit gekozen kan worden
        lijst.append(i)
    
    #Laat het network zien
    nx.draw(network)

star_graph(5,400,4)