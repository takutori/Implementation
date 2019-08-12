import numpy as np
import matplotlib.pyplot as plt
import pdb

X = []
Y = []

start = -1-np.sqrt(6)/3+0.01
goal = -1+np.sqrt(6)/3-0.01

for x in np.arange(start,goal,0.01):
        X.append(x)
        t = -3*(x**2) -6*x + 1
        Y.append( (x-1 + np.sqrt(t))/2 )

        X.append(x)
        Y.append( (1-x + np.sqrt(t))/2 )

        #pdb.set_trace()

plt.scatter(X,Y)
plt.show()