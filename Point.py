import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self, x_ref,y_ref):
        d = np.sqrt(
            (self.x - x_ref)**2 + (self.y - y_ref)**2
        )
        return d
        
    def plot(self, color="black", shape = "*"):
        plt.gca().plot(self.x,self.y,
                       shape,
                       color=color)
