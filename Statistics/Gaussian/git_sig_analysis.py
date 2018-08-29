import numpy as np


def singular_analysis(data):
    if len(data[:,0]) == len(data[0,:]):
        print('data = \n %s'% data)
        print('output Covariance and Diagonalization')
        Cov = np.cov(data)
        a,P = np.linalg.eig(data)
        A = np.diag(a)
        P_1 = np.linalg.inv(P)
        PAP_1 = np.dot(P,np.dot(A,P_1))
        print('Covariance = \n %s'% Cov)
        print('Diagonalization \n P= \n %s'% P)
        print('intrinsic = \n A= \n %s'% A)
        print('P_inv = \n %s'% P_1)

    else:
        print('data = \n %s'% data)
        print('output Covariance and Singular value decomposition')
        Cov = np.cov(data)
        U,singular,V = np.linalg.svd(data)
        print('Covariance = \n %s'% Cov)
        print('Singular value decomposition')
        print('U = \n %s'% U)
        print('singular value = \n %s'% singular)
        print('V_T = %s'% V.T)

    print('data = \n')
    return data
