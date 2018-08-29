import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import pdb




# Logistic sigmoid function
def sigmoid(a):
    _return = 1/(1+np.exp(-a))
    return _return


class Logistic:

    def __init__(self,tra_d,tra_r):
        self.tra_d = tra_d;
        self.tra_r = tra_r;

    def fit(self,):
        num = self.tra_d.shape[0]
        dim = self.tra_d.shape[1]

        # a_n
        def make_a(w):
            a = np.zeros((num,1))
            for i in range(num):
                a[i] = np.dot(w.T,self.tra_d[i,:].T)
            return a
        # y_n
        def make_y(a):
            y = np.zeros((num,1))
            for i in range(num):
                y[i] = sigmoid(a[i])
            return y

        # Cross entropy error function
        def CEEF(w):
            error = 0
            a = make_a(w)
            y = make_y(a)
            for i in range(num):
                error = error - (self.tra_r[i]*np.log(y[i]) + (1-self.tra_r[i])*np.log(1-y[i]))
            return error[0]


        # Iterative reweighted least squares method
        def IRLS():
            print('Start Iterative Rewighted Least Squares Method\n')
            convage = 0.5
            print('This algorithm is regard as convaging w less %s'%convage)
            # init value of w
            w = np.zeros((dim,1))
            # empty list for identfying declile CEEF value
            CEEF_value = []
            step = []
            # estimate w by Newton's method
            for iteration in range(1000):
                # a_n
                a = make_a(w)
                # y_n
                y = make_y(a)

                # R
                R = np.zeros((num,num))
                for i in range(num):
                    R[i,i] = y[i]*(1-y[i])

                # hessian matrix
                H = np.dot(np.dot(self.tra_d.T,R),self.tra_d)

                # z
                z = np.dot(self.tra_d,w) - np.dot(np.linalg.inv(R),y-self.tra_r)

                # update w
                H_inv = np.linalg.inv(H)
                w_new = np.dot(np.dot(np.dot(H_inv,self.tra_d.T),R),z)
                print('w is updated')
                step.append(iteration)
                CEEF_value.append(CEEF(w_new))

                if abs(CEEF(w)-CEEF(w_new)) < convage:
                    print('w is convaged!!!!!!!!!\n')
                    print('cross entropy error function value is : %s\n'%CEEF(w_new))
                    break
                else:
                    w = w_new

                if iteration%100==0 and iteration!=0:
                    print('This algorythm is estimaiting %s times now....\n'%iteration)

            print('OK, estimation is complicated!\n')

            plot = input('Do you plot relationsihp of iteration times and Closs entropy error function?  (YES or NO) :')
            if plot=='YES':
                imagename = input('Please name to save image:  ')
                imagepath = os.path.join('../../dataset/implementation/Logistic/','%s.png'%imagename)
                plt.scatter(step,CEEF_value,s=20,c='red',marker='x')
                plt.savefig(imagepath)
                print('OK, image saving is complicated!\n')

            return w

        best_w = IRLS()

        def decition_function(x):
            P = sigmoid(np.dot(best_w.T,x.T))
            return P

        return decition_function


    def predict(self,tes_d,decition_function):
        num = tes_d.shape[0]
        print('Start predict test data\n')
        P = np.zeros((num,1))
        predi = np.zeros((num,1))
        for i in range(tes_d.shape[0]):
            P[i] = decition_function(tes_d[i,:])
            if P[i] > 0.5:
                predi[i] = 1
        print('OK, predicting is complicated!')

        display = input('Do you want to identify reslut of estimation?  (YES or NO)')
        if display == 'YES':
            print('OK, will show you Category and its Probablity\n')
            P_list = []
            predict_list = []
            for i in range(tes_d.shape[0]):
                P_list.append(round(P[i,0],4))
                predict_list.append(predi[i])
                pd_result = pd.DataFrame({'Predict':predict_list,'P':P_list})
            print(pd_result)

        return P,predi

    def check(self,P,predi,tes_r):
        num = tes_r.shape[0]
        c = 0
        for i in range(num):
            if predi[i] == tes_r[i]:
                c = c + 1
            else:
                c = c + 0
        rate = c/tes_r.shape[0]
        print('checking percentage is complicated!\n')

        display = input('Do you want to identify reslut of estimation with correct answer?  (YES or NO)')
        if display == 'YES':
            print('OK, will show you Probablity and estimation and correct answer\n')
            P_list = []
            predict_list = []
            test_ans_list = []
            for i in range(tes_r.shape[0]):
                P_list.append(round(P[i,0],4))
                predict_list.append(predi[i])
                test_ans_list.append(tes_r[i])
            pd_result = pd.DataFrame({'correct':test_ans_list,'predict':predict_list,'P':P_list})

            print(pd_result)

        print('percentage of correct answer :  %s'%rate)
        
        return rate
