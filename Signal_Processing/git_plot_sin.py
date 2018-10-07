import numpy as np
import matplotlib.pyplot as plt
from DFT_def import DFT


def genSine(A, f, phi, fs, t):
    T = np.arange(0,t,1/fs)
    X = A*np.cos(2*np.pi*f*T+phi)
    return X


def main():

    A = 1
    f = 10.0
    phi = 1.0
    fs = 50.0
    t = 1

    X = genSine(A,f,phi,fs,t)
    Y = DFT(X)
    x_axis = np.arange(len(X))
    plt.subplot(2, 1, 1)
    plt.plot(x_axis,X)
    plt.title('before DFT')

    plt.subplot(2, 1, 2)
    plt.plot(x_axis,Y)
    plt.title('after DFT')

    plt.tight_layout()
    plt.savefig('../../../dataset/signal_processing/image/DFT.png')


if __name__ == '__main__':
    main()
