import numpy as np



def AND(X):
    W = np.array([0.5,0.5])
    b = -0.7
    tmp = np.dot(W,X.T)+b
    if tmp <= 0:
        return 0
    elif tmp >= 0:
        return 1



def NAND(X):
    W = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.dot(W,X.T)+b
    if tmp <= 0:
        return 0
    elif tmp >= 0:
        return 1

def OR(X):
    W = np.array([0.5,0.5])
    b = -0.2
    tmp = np.dot(W,X.T)+b
    if tmp <= 0:
        return 0
    elif tmp >= 0:
        return 1


def XOR(X):
    X_2 = np.array([OR(X),NAND(X)]) #二層目の値
    tmp = AND(X_2)
    if tmp <= 0:
        return 0
    if tmp >= 0:
        return 1
