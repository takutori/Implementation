import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pdb
import pandas as pd

def f(X):
    x = X[0,0]
    v = X[1,0]
    y = X[2,0]
    w = X[3,0]
    k = 2.0
    def F_1(a,b,c):
        return -k*a - 0.01*b*np.sqrt(b**2+c**2)
    def F_2(a,b,c):
        return -0.1*9.8 - k*a - c*np.sqrt(b**2+c**2)

    _return = np.zeros((4,1))
    _return[0,0] = v
    _return[1,0] = F_1(x,v,w)/0.1
    _return[2,0] = w
    _return[3,0] = F_2(y,v,w)/0.1
    return _return


def Euler(f,x_0,t_0=0,T=3.0,h=3.0/200.0):
    x_old = x_0
    update_list = x_0
    for t in np.arange(t_0,T,h):
        x_new = x_old + h*f(x_old)
        x_old = x_new
        update_list = np.concatenate((update_list,x_new),axis=1)
    return update_list

def main():

    X_0 = np.array([[0.0,5.0,1.0,1.0]]).T
    answer = Euler(f,X_0)
    answer_df = pd.DataFrame(answer).rename(index={'0':'x','1':'v','2':'y','3':'w'})
    print(answer_df)
    #plt.scatter(answer[0,:],answer[2,:],s=2.0)
    #plt.savefig('../../dataset/implementation/Numeric/Euler_method_example.png')

    fig = plt.figure()
    ims = []
    for n in range(len(answer[0,:])):
        plot_array = np.array([answer[0,0:n+1],answer[2,0:n+1]])
        plt.xlim(-1-0.5,1+0.5)
        plt.ylim(-0.5-0.5,1+0.5)
        im = plt.plot(plot_array[0,:],plot_array[1,:],c='black')
        ims.append(im)
    ani = animation.ArtistAnimation(fig, ims, interval=50)
    ani.save("../../dataset/implementation/Numeric/Euler_method_example.gif", writer="imagemagick")

if __name__ == '__main__':
    main()
