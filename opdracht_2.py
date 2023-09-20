import numpy as np
import matplotlib.pyplot as plt

def draw_mandel(width):
    height = width
    x_min, x_max = -1.5, 0.5
    y_min, y_max = -1, 1
    max_iterations = 100
    mandelbrot_set = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            x = x_min + (x_max - x_min) * i / (width - 1)
            y = y_min + (y_max - y_min) * j / (height - 1)
            c = complex(x,y)
        

            z = 0
            for n in range(max_iterations):
                if abs(z) > 2:
                    mandelbrot_set[i, j] = n
                    break
                z = z * z + c

    plt.imshow(mandelbrot_set)
    plt.show()
            
draw_mandel(200)