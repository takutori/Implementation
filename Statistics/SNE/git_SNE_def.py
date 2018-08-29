import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import matplotlib.pyplot as plt
import pdb
import os


def Robbins_monro(function,grad,number,target_dim):
    print('start Robbins monro algorithm\n')
    init_eta = 0.5
    print('initial learning rate is %s\n'%init_eta)
    stepsize = 1000
    print('max stepsize is %s\n'%stepsize)
    place = 3
    print('This algorithm try to estimate best solution from %s place \n'%place)
    convage = 0.01
    print('This program regard less %s as convaging estimaion'%convage)

    for iteration in range(place):
        init_value = np.random.randn(number,target_dim)
        old_estimation = init_value
        place_est = init_value
        init_eta = 0.5

        for step in range(1,stepsize+1):
            n_rate = init_eta/step
            new_estimation = old_estimation - n_rate*grad(old_estimation)

            # costfunction　が減っているかの確認
            #if step%10 == 0:
            print('Cost Function :  %s\n'%function(new_estimation))

            if abs(function(old_estimation) - function(new_estimation)) < convage:
                print('solution convage\n')
                break
            else:
                old_estimation = new_estimation


        Elapsed= round(iteration/place,2)
        print('%s s percent is succeed!\n'%Elapsed)
        if function(place_est) > function(new_estimation):
            place_est = new_estimation

    print('estimation is complicated!\n')

    return place_est



class SNE:
    def __init__(self,X):
        self.data = X;
        self.number = X.shape[0];
        self.dim = X.shape[1];



    def plot(self,filename):

        target_dim = int(input('dim  : '))
        sigma = float(input('sigma  : '))

        d_name = input('distance name = Eclid:E , Mahalanobis:M \n Choice distance name :')
        if d_name == 'E':
            def d(X,i,j):
                distance = sum((X[i,:]-X[j,:])**2)
                return distance
        if d_name == 'M':
            def d(X,i,j):
                Sigma = np.cov(X)
                Sigma_inv = np.linalg.inv(Sigma)
                distance = np.dot(np.dot(X[i,:]-X[j,:],Sigma_inv),(X[i,:]-X[j,:]).T)
                return distance

        def d_ij(i,j,sigma):
            dissimi = (d(self.data,i,j))//(2*(sigma**2))
            return dissimi

        def P_ij(i,j,sigma):
            numerator = np.exp(-d_ij(i,j,sigma))
            denominator = -1
            for k in range(self.number):
                denominator = denominator + np.exp(-d_ij(i,k,sigma))
            return numerator/denominator

        def Q_ij(Y,i,j):
            numerator = np.exp(-d(Y,i,j))
            denominator = -1
            for k in range(Y.shape[0]):
                denominator = denominator + np.exp(-d(Y,i,k))
            return numerator/denominator


        def costfunction(Y):
            C = 0
            for n in range(self.number):
                for m in range(self.number):
                    if n != m:
                        P = P_ij(n,m,sigma)
                        Q = Q_ij(Y,n,m)
                        C = C + P*(np.log(P/Q))
            return C

        def partial(Y):
            partialY = np.zeros((self.number,target_dim))
            for n in range(self.number):
                partialy = np.zeros((1,target_dim))
                for m in range(self.number):
                    if n != m:
                        partialy = partialy + 2*(Y[n,:]-Y[m,:])*(P_ij(n,m,sigma)-Q_ij(Y,n,m)+P_ij(m,n,sigma)-Q_ij(Y,m,n))
                        partialY[n,:] = partialy
            return partialY

        embeding = Robbins_monro(costfunction,partial,self.number,target_dim)

        if target_dim == 2:
            file = filename.split(".")[0]
            imagename = '{name}_S-{sig}_D-{dista}'.format(name=file,sig=sigma,dista=d_name)
            plt.scatter(embeding[:,0],embeding[:,1])
            imagepath = os.path.join('../../dataset/gene/plot','%s.png'%imagename)
            plt.savefig(imagepath)

        else:
            print('please dimention is 2\n')

        print('saving image is comlicated!\n')
        return embeding
