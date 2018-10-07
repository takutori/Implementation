import numpy as np



def DFT(x):
    ans=[]
    N = x.size
    for k in range(N):
        s = np.exp(1j * 2 * np.pi * k/N * np.arange(N))
        ans = np.append(ans, sum(x * np.conjugate(s)))
    return np.array(ans)


def IDFT(X):
    ans = []
    N = X.size
    for k in range(N):
        s = np.exp(1j * 2 * np.pi * k/N * np.arange(N))
        ans = np.append(ans, 1 / N * sum(X * s))
    return np.array(ans)
