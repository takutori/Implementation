import numpy as np
import sys
import os
from SVM_def import SVM
import pdb
import matplotlib.pyplot as plt


def main():
    data_type = input('which do you use data type (circle or random)? :')
    if data_type == 'circle':
        tra_d = np.load('../../dataset/Implementation/Sampletest/circle_training_data.npy')
        tra_r = np.load('../../dataset/Implementation/Sampletest/circle_training_r.npy')
        T = np.load('../../dataset/Implementation/Sampletest/circle_T.npy')
    elif data_type == 'random':
        tra_d = np.load('../../dataset/Implementation/Sampletest/noliner_training_data.npy')
        tra_r = np.load('../../dataset/Implementation/Sampletest/noliner_training_r.npy')
        T = np.load('../../dataset/Implementation/Sampletest/noliner_T.npy')


    print('Start SVM algorithm\n')
    test = SVM(tra_d,tra_r)
    f,W,b,C,kernel_name = test.fit()

    x = np.linspace(-6,6,100)
    y = np.linspace(-6,6,100)
    X,Y = np.meshgrid(x,y)
    w,h = X.shape
    X.resize(X.size)
    Y.resize(Y.size)
    Z = np.array([f(np.array([x_1,y_1])) for (x_1,y_1) in zip(X,Y)])
    X.resize((w,h))
    Y.resize((w,h))
    Z.resize((w,h))
    plt.contour(X,Y,Z,[0.0],colors='k',linewidths=1)

    plt.scatter(tra_d[T==1,0],tra_d[T==1,1],label='C_1',c='red',marker='x',s=5)
    plt.scatter(tra_d[T==-1,0],tra_d[T==-1,1],label='C_2',c='blue',marker='x',s=5)
    plt.title('{}-data {} SVM  C={}'.format(data_type,kernel_name,str(C)))
    plt.legend()
    plt.savefig('../../dataset/Implementation/SVM/image/{}_SVM_K-{}_C-{}.png'.format(data_type,kernel_name,C))
    print('saving fig is complicated\n')

    print('Algorithm is finished\n')

if __name__ == '__main__':
    main()
