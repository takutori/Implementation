import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt


x = np.arange(-5,5,0.01)
Sigma = np.arange(1,5,0.5)
mu = 0
for sigma in Sigma:
    f = 1/(np.sqrt(2*np.pi*(sigma**2)))*np.exp((-(x-mu)**2)/(2*(sigma**2)))
    plt.plot(x,f,label=sigma)
    plt.legend()
plt.savefig('../dataset/py_study/gausu_distribution.png')


for sigma in Sigma:
    mu = 0
    x = np.arange(-5,5,0.1)
    g = (1/2)*(1+erf((x-mu)/np.sqrt(2*(sigma**2))))
    plt.plot(x,g,label=sigma)
    plt.legend()
plt.savefig('../dataset/py_study/accumulated_gausu.png')
