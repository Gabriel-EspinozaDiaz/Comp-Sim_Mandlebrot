import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors as clr

class Mandelbrot:

    def __init__(self,N):
    
        self.limit = N

        self.xmin = -2.025
        self.xmax = 0.6
        self.ymin = -1.125
        self.ymax = 1.125
        self.points = 512

        self.matrix = np.zeros((self.points,self.points))

    def run(self):
        """
        Obtains all coordinates from list_parameters() and iterates through them
        On each iteration, uses find_limit to determine how many iterations it takes x+yj to exceed self.limit
        Stores the count of iterations in self.matrix
        Runs graph() at the end
        """
        xpars = Mandelbrot.list_parameters(self)[0]
        ypars = Mandelbrot.list_parameters(self)[1]

        for x in range(self.points):
            for y in range(self.points):
                self.matrix[y][x] = Mandelbrot.find_limit(self,complex(xpars[x],ypars[y]))
        
        Mandelbrot.graph(self)

    def list_parameters(self):
        """
        Determines the distance between each point based on the number of points being presented on the graph, and the limits being evaluated. 
        Returns a list containing 2 nested lists, each with the paremeters (C) of the x and y, respectively
        """
        xdist = abs(self.xmax - self.xmin)/self.points
        ydist = abs(self.ymax - self.ymin)/self.points
        xpars = []
        ypars = []
        for n in range(self.points):
            xpars.append(self.xmin+xdist*n)
            ypars.append(self.ymin+ydist*n)
        return [xpars,ypars]

    def find_limit(self,c):
        """
        Runs the mandelbrot recursive formula on parameter c, and returns the number of iterations within self.limit taken to exceed an absolute value of 2
        Otherwise returns self.limit
        """
        z = 0
        for n in range(self.limit):
            z = z**2 + c
            if abs(z) > 2:
                return n
        return self.limit
    
    def graph(self):
        """
        Uses matplotlib heatmap to graph self.matrix, with x/y mins and maxes as axes guides
        """
        plt.imshow(self.matrix,extent=(self.xmin,self.xmax,self.ymin,self.ymax),cmap='coolwarm',interpolation='none',origin='lower')
        plt.colorbar()
        plt.show()

class main():
    X = Mandelbrot(255)
    X.run()

