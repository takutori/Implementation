import numpy as np
import matplotlib.pyplot as plt
import pdb

class DFT:
    def __init__(self,signal):
        self.signal = signal
        self.dft = []
        self.idft = []

    def DFT(self,signal=[],plot=False):
        if len(signal) != 0:
            self.dft = signal
            self.signal = signal
        ans=[]
        N = len(self.signal)
        for k in range(N):
            s = np.exp(1j * 2 * np.pi * k/N * np.arange(N))
            ans = np.append(ans, sum(self.signal * np.conjugate(s)))
        self.dft = np.array(ans)

        if plot == True:
            plt.plot(np.arange(len(self.dft)),self.dft,color='green')
            plt.show()

    def IDFT(self,signal=[],plot=False):
        if len(signal) != 0:
            self.idft = signal
        ans = []
        if len(self.dft) == 0:
            print('Error: not exist idft')
        else:
            N = len(self.dft)
            for k in range(N):
                s = np.exp(1j * 2 * np.pi * k/N * np.arange(N))
                ans = np.append(ans, 1 / N * sum(self.dft * s))
            self.idft =  np.array(ans)
        if plot == True:
            T = np.arange(0,2*np.pi,2*np.pi/len(self.signal))
            pdb.set_trace()
            plt.plot(T,self.idft,color='green')
            plt.show()

    def FFT(self):
        """
        N = len(self.signal)
        if N%2 != 0:
            print('Error: sumple size is not even number, so please use not FFT but DFT. ')
        else:
            W = np.exp(-1*1j * ((2*np.pi)/N))
            count = 0
            M = N
            for i in range(100000):
                if M%2 == 0 :
                    M = M/2
                    count = count + 1
                else:
                    break

            m = N/(2**count)
            #N expressed as N = (2**count) * m
            for index in range(m):
                X = np.zeros((m,m))
                for i in range(m):
                    for j in ragen(m):
                        X[i,j] = W**(i*count*j)
            network = {'X_'+str(index):X}
        """
        




    def plot(self):
        T = np.arange(0,2*np.pi,2*np.pi/len(self.signal))
        plt.figure(figsize=(3,4))
        plt.subplot(2,1,1)
        plt.plot(T,self.signal,color='green')

        plt.subplot(2,1,2)
        plt.plot(np.arange(len(self.dft)),self.dft,color='green')

        plt.show()
