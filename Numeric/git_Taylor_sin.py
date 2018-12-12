import numpy as np
import matplotlib.pyplot as plt

import pdb
import matplotlib.animation as animation

def f(x):
    return np.sin(x)

def diff(f,x):
    h = 0.001
    return (f(x+h)-f(x))/h

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

import pdb
def Taylor(f,N,x):
    tay = 0
    for n in range(N):
        tay = tay + ((np.sin((n/2)*np.pi))/factorial(n))*(x**n)
    return tay

def main():
    fig = plt.figure()
    ims = []

    X = np.arange(-np.pi,np.pi,0.01)
    sin_curve = f(X)
    for N in range(1,11):
        Appr = np.array([Taylor(f,N,x) for x in X])
        plt.plot(X,np.sin(X))
        im = plt.plot(X,Appr,color='r')
        ims.append(im)
    ani = animation.ArtistAnimation(fig, ims, interval=100)
    ani.save("../../Taylor_sin.gif", writer="imagemagick")

if __name__ == '__main__':
    main()
