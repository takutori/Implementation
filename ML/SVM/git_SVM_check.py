import numpy as np
import sys
import os
from SVM_def import SVM
import pdb
import matplotlib.pyplot as plt

tra_d = np.load('../../dataset/Implementation/Sampletest/training_data.npy')
tra_r = np.load('../../dataset/Implementation/Sampletest/training_r.npy')
T = np.load('../../dataset/Implementation/Sampletest/T.npy')
def main():

    print('Start SVM algorithm\n')
    test = SVM(tra_d,tra_r)
    f,W,b,C,kernel_name = test.fit()

    W = W.reshape((1,2))
    w_1 = W[0,0]
    w_2 = W[0,1]
    def hyper_plane(x):
        return -(w_1/w_2)*x-b/w_2

    x_axis = np.arange(tra_d[:,0].min()-1,tra_d[:,0].max()+1,0.1)
    line = [hyper_plane(i) for i in x_axis]
    plt.scatter(tra_d[T==1,0],tra_d[T==1,1],label='C_1',c='red',marker='x',s=5)
    plt.scatter(tra_d[T==-1,0],tra_d[T==-1,1],label='C_2',c='blue',marker='x',s=5)
    plt.plot(x_axis,line)
    plt.title('{} SVM  C={}'.format(kernel_name,str(C)))
    plt.legend()
    plt.savefig('../../dataset/Implementation/SVM/image/SVM_test.png')
    print('saving fig is complicated\n')

    print('Algorithm is finished\n')

if __name__ == '__main__':
    main()
