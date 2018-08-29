import numpy as np
import matplotlib.pyplot as plt


def bef_afscatter(afdata,befdata):

    print('save scatterplot of newdata and transformed data')
    plt.scatter(afdata[0,:],afdata[1,:],s=5,color='black',label='afterdata')
    plt.scatter(befdata[0,:],befdata[1,:],s=5,color='blue',label='beforedata')
    plt.legend()
    plt.savefig('../../dataset/py_study/test_plot.png')



def cal_w(data):
    print('I output transform matrix of this data\n')
    print('firstly, calculation of cobariance and display cobariance as Sigma\n')
    Sigma = np.cov(data)
    print('sigma=%s\n'%Sigma)
    print('secondly, I do calculation diagonalisation of this Sigma \n and display transform matrix\n')
    a,P = np.linalg.eig(Sigma)
    A = np.diag(a)
    A_half = np.sqrt(A)
    W = np.dot(P,A_half)
    print('transforming matrix = %s'%W)

    return W

def gausu_double():
    mu = np.array([0,0])
    cov = np.array([[1,0],[0,1]])
    data = np.random.multivariate_normal(mu,cov,1000)
    return data
