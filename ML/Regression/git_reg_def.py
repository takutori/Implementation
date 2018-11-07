import numpy as np
import matplotlib.pyplot as plt
import pdb


class polynomial_fit:
    def __init__(self,train_d_set,train_t_set):
        self.train_d_set = train_d_set
        self.train_t_set = train_t_set
        #self.mean = 0
        #self.sigma = 0
        #self.model = 0

    def Bayesian_fit(self,M,alpha=0.005,beta=11.1):
        N = len(self.train_d_set)
        self.M = M
        self.alpha = alpha
        self.beta = beta

        phi = np.zeros((N,M)) #phi_ij = x_i**jをもつ行列
        for n in range(N):
            for m in range(M):
                phi[n,m] = (self.train_d_set[n])**m

        phi_t = 0
        for n in range(N):
            phi_t = phi_t + phi[n,:]*self.train_t_set[n]

        phi_phi = 0
        for n in range(N):
            vector = phi[n,:].reshape((1,M))
            phi_phi = phi_phi + np.dot(vector.T,vector)

        S_inv = alpha*np.eye(M)+beta*phi_phi
        S = np.linalg.inv(S_inv)

        def mean(x):
            phi_x = np.array([x**m for m in range(M)])
            mean = beta*np.dot(np.dot(phi_x,S),phi_t.T)
            return mean
        self.mean = mean
        def sigma(x):
            phi_x = np.array([x**m for m in range(M)]).reshape((1,M))
            sigma = beta**(-1) + np.dot(np.dot(phi_x,S),phi_x.T)
            sigma = sigma[0,0]
            return sigma
        self.sigma = sigma

        def model(X):
            t = (1/(np.sqrt(2*np.pi) * sigma(X))) * np.exp((-(X-mean(X))**2)/(2*(sigma(X)**2)))
            return t
        self.model = model


    def plot(self,path='../../../dataset/implementation/ML/Regression/image',filename):
        min_x = np.min(self.train_d_set)
        max_x = np.max(self.train_d_set)
        x_axis = np.arange(min_x,max_x,0.01)
        mean_box = []
        mean_plussd = []
        mean_minussd = []
        target_box = []
        for x in x_axis:
            y = self.mean(x)
            mean_box.append(y)
            mean_plussd.append(y+np.sqrt(self.sigma(x)))
            mean_minussd.append(y-np.sqrt(self.sigma(x)))
            yy = self.model(x)
            target_box.append(yy)

        plt.plot(x_axis,mean_box,color='red',label='mean')
        plt.fill_between(x_axis,mean_minussd,mean_plussd,facecolor='red',alpha=0.1)
        plt.scatter(self.train_d_set,self.train_t_set,color='blue',marker='x')
        plt.ylim(min(self.train_t_set)-1.5,max(self.train_t_set)+1.5)
        plt.legend()
        plt.title('order={}, alpha={}, beta={}, sample={}'.format(self.M,self.alpha,self.beta,len(self.train_d_set)))


        imagename = 'file={}-beyesian_fit_sampleN-{}_order-{}_alpha-{}_beta-{}.png'.format(filename,len(self.train_d_set),self.M,self.alpha,p_beta)
        path_name = path+'/'+filename
        plt.savefig(path)
