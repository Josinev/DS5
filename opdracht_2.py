import numpy as np
import matplotlib.pyplot as plt

n = []
i = 0
for i in range(101):
    n.append(i)
    i += 1

a_n = []

x = np.random.uniform(-1.5, 0.5)
y = np.random.uniform()

c = complex(x,y)
print(c)

for n in range(101):
    if n == 0:
        a_n.append(0)
    else:
        a_n.append((n - 1) **2 + c)

print(a_n)