import numpy as np


def function(data):
    x = data[0]
    y = data[1]
    return (x-3)**2 + (y-2)**2



def grad(data):
    x = data[0]
    y = data[1]
    grad = np.array([3*(x-3),2*(y-2)])
    return grad
