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
