import numpy as np

from reg_def import polynomial_fit




def main():
    X = np.arange(0,2*np.pi,2*np.pi/100)
    Y = np.sin(X)+0.3*np.random.randn(len(X))


    for iter in range(10,100,10):
        verb_model = polynomial_fit(X[0,iter],Y[iter])
        verb_model.Bayesian_fit(M=4,alpha=0.005,beta=1)
        verb_model.plot(filename='verb_sin')

if __name__ == '__main__':
    main()
