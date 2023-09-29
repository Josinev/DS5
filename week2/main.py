import numpy as np
import matplotlib.pyplot as plt

"""Opdracht 1"""
def records(file_path):
    """Lijst maken van het geimporteerde csv bestand met de cijfers van een klas."""
    records = []
    with open(file_path, 'r') as file:
      csv_reader = csv.DictReader(file)
      for row in csv_reader:
        records.append(row)
def average(records):
    """ bereken het gemiddelde door alle recods bij elkaar op te tellen en te delen door het totaal"""
    total = sum(float(record['Grade']) for record in records)
    average = total / len(records)

    print(f"Average Grade: {average}")
    print("--------------------")
def filter(records):
    """Wanneer cijfer hoger is dan 80.0 dan print name en cijfer student"""
    filtered_records = [record for record in records if float(record['Grade']) >= 80.0]

    print("Student Report")
    print("--------------")
    for record in filtered_records:
        print(f"Name: {record['Name']}")
        print(f"Grade: {record['Grade']}")
        print("--------------------")
file_path = input("Enter the path to the CSV file: ")

"""Opdracht 2"""
import numpy as np
import matplotlib.pyplot as plt

def draw_mandel(lengte):
    ''' Tekent een mandelbrot plaatje
    input: lengte van de mandelbrot
    output: plaatje mandelbrot'''
    breedte = lengte
    #minimum en maximum waardes van x en y
    xmin= -1.5
    xmax= 0.5
    ymin= -1
    ymax = 1
    aantal_herhalingen = 100
    #Maakt lege set met alleen maar nullen
    mandelbrot_set = np.zeros((lengte, breedte))
    
    #Met deze forloop komen en 200 gelijke stapjes tussen xmin en xmax
    #Hetzelfde geldt voor ymin en ymax
    for i in range(lengte):
        for j in range(breedte):
            x = xmin + (xmax - xmin) * i / (lengte - 1)
            y = ymin + (ymax - ymin) * j / (breedte - 1)
            #Maakt complex getal
            c = complex(x,y)
        
            #a_n = a_n-1 ** 2 + c
            z = 0
            for n in range(aantal_herhalingen):
                if abs(z) > 2:
                    mandelbrot_set[i, j] = n
                    break
                z = z ** 2 + c

    #Maakt daadwerkelijk het plaatje
    plt.imshow(mandelbrot_set)
    plt.show()
            
draw_mandel(200)


"""Opdracht 3.1"""
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

"""Opdracht 3.2"""
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
