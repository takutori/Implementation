import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pdb
import scipy.constants
from scipy import integrate




def variational_F(b,A):

    def F(x):
        t = x*2*np.pi
        du_dx = b + 8*(A/100)*(np.sin(8*t))
        return np.sqrt(1+du_dx**2)
    value,error = integrate.quad(F, 0, 1)
    return value



def curve(A,b,x):
    t = x*2*np.pi
    y = b*x + (A/100)*(np.sin(8*t))
    return y


def solution_curve(b,x):
    return b*x



def main():

    goal = int(input('goal value at x=1: '))
    T = np.arange(0,1,0.01)

    fig, (ax1, ax2) = plt.subplots(2,1)
    ims = []
    A_list = [abs(50 - i%100) for i in range(501)]
    count = 0
    color_list = ['blue','red']
    value_integ = []
    value_integ_xaxis = []
    for A in A_list:
        false_y = []
        true_y = []
        for t in T:
            f_y = curve(A,goal,t)
            false_y.append(f_y)
            t_y = solution_curve(goal,t)
            true_y.append(t_y)

        value_integ_xaxis.append(A/100)
        value_integ.append(variational_F(goal,A))

        if A==0:
            color_r = color_list[1]
        else:
            color_r = color_list[0]
        #plt.xlim(0,1+0.3)
        #plt.ylim(goal-0.3,0)
        im1, = ax1.plot(T,false_y,color=color_r)
        #im1, = ax1.plot(true_x,true_y,color='red')
        #im1 = plt.title('curve')
        #plt.xlim(0,len(A_list))
        im2, = ax2.plot([value_integ_xaxis[count]],[value_integ[count]],color=color_r,marker='o')
        #im2, = ax2.plot(A_list,[parm for i in range(len(A_list))],color='red')
        #im2 = plt.title('Euler Equation')

        ims.append([im1,im2])

        count = count + 1
    ani = animation.ArtistAnimation(fig, ims, interval=100,blit=False,repeat=True)
    ani.save("../../dataset/implementation/Optimization/image/line_variational.gif", writer="imagemagick")





if __name__ == '__main__':
    main()
