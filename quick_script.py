import numpy as np
import matplotlib.pyplot as plt
from Point import Point


x = np.r_[0:10]
y = 3*x + 5

print(np.c_[x,y])

plt.figure()

for z in zip (x,y):
    p = Point(z[0], z[1])
    print(z[0],z[1], p.x,p.y, p.distance(0,0) )

    p.plot(color='red',shape='s')

plt.savefig('points.png')
