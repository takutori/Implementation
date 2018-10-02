import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pdb
import scipy.constants
from scipy import integrate


def Euler(parm,A,t):

    x_dt = 0.5*parm*(1-np.cos(t))
    y_dt = -0.5*parm*np.cos(t)+((8*A)/100)*np.cos(8*t)
    y = -0.5*parm*(1-np.cos(t)) + (A/100)*np.sin(8*t)
    euler_form = (1+(y_dt/x_dt)**2)*(-y)
        #numerator = np.sqrt(x_dt**2+x_dt*y_dt)
        #denominetor = np.sqrt(-2*scipy.constants.g*y)
    return euler_form #numerator/denominetor

    #return value

def variational_F(parm,A):

    def F(t):
        x_dt = parm*(1-np.cos(t))
        y_dt = parm*np.sin(t)+((8*A)/100)*np.cos(8*t)
        y = parm*(1-np.cos(t)) + (A/100)*np.sin(8*t)
        numerator = np.sqrt(x_dt**2+x_dt*y_dt)
        denominator = np.sqrt(-2*scipy.constants.g*y)
        return numerator/denominator

    value,error = integrate.quad(F, 0, 2*np.pi)

    return value


def curve(parm,A,t):
    x = parm*(t-np.sin(t))
    y = parm*(1-np.cos(t)) + (A/100)*np.sin(8*t) #- (A**2)*np.sin(2*t) + (A**3)*np.sin(3*t) #- (A**4)*np.sin(4*t) + (A**5)*np.sin(5*t) - (A**6)*np.sin(6*t)
    #print('np.sin(A*t): %s'%np.sin(A*t))
    return (x,y)


def solution_curve(parm,t):
    x = parm*(t-np.sin(t))
    y = parm*(1-np.cos(t))
    return (x,y)


def main():

    goal_x = int(input('goal value at x axis: '))
    #goal_y = int(input('goal value at y axis: '))
    T = np.arange(0,2*np.pi+2*np.pi/1000,2*np.pi/1000)
    parm = goal_x/(2*np.pi)

    fig, (ax1, ax2) = plt.subplots(2,1)
    ims = []
    A_list = [abs(50 - i%100) for i in range(501)]
    count = 0
    color_list = ['blue','red']
    for A in A_list:
        false_x = []
        false_y = []
        true_x = []
        true_y = []
        euler_xaxis = []
        euler_plot = []
        for t in T:
            f_x,f_y = curve(parm,A,t)
            false_x.append(f_x)
            false_y.append(f_y)
            t_x,t_y = solution_curve(parm,t)
            true_x.append(t_x)
            true_y.append(t_y)

            euler_xaxis.append(A/100)
            euler_plot.append(variational_F(parm,A))


        if A==0:
            color_r = color_list[1]
        else:
            color_r = color_list[0]
        #plt.xlim(0,1+0.3)
        #plt.ylim(goal-0.3,0)
        im1, = ax1.plot(false_x,false_y,color=color_r)
        #im1, = ax1.plot(true_x,true_y,color='red')
        #im1 = plt.title('curve')
        #plt.xlim(0,len(A_list))
        im2, = ax2.plot(euler_xaxis,euler_plot,color=color_r)
        #im2, = ax2.plot(A_list,[parm for i in range(len(A_list))],color='red')
        #im2 = plt.title('Euler Equation')

        ims.append([im1,im2])

        count = count + 1
    ani = animation.ArtistAnimation(fig, ims, interval=100,blit=False,repeat=True)
    ani.save("../../dataset/implementation/Optimization/image/variational.gif", writer="imagemagick")





if __name__ == '__main__':
    main()
