import numpy as np
import matplotlib as plt

class Mandlebrot:

    def __init__(self,N):

        self.limit = N
        self.xC = 0.4
        self.yC = 0.4


        x= 0
        y= 0
        coords = []
        count = 0
        while count < N:
            coords.append(complex(x,y))
            x = next(x,self.xC)
            y = next(y,self.yC)
            count += 1
        print(coords)



    def next(p,C):
        pn = p**2+C
        return pn
    
        


"""
NOTES:
Recommended ranges: x={-2.025 → 0.6} and y={-1.125 → 1.125}

"""

    
class main():
    print(Mandlebrot(255))