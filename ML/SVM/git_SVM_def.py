import numpy as np
import pandas as pd
import pdb


def IPM(X,Y,kernel,C):
    print('Start algorithm of Imterror Point Method\n')
    num = X.shape[0]
    convage = 1e-8
    print('This algorithm regard solution as convaging solution if update amount less %s'%convage)
    def diag(x):
        Di = np.zeros((num,num))
        for i in range(num):
            Di[i,i] = x[i]
        return Di

    Q = np.zeros((num,num))
    for i in range(num):
        for j in range(num):
            Q[i,j] = Y[i]*Y[j]*kernel(i,j)

    def make_r_1(alpha,b,epsilon,s):
        return np.dot(Q,alpha) + Y*b + epsilon - 1 - s
    def make_r_2(alpha):
        return np.dot(Y.T,alpha)
    def make_r_3(alpha,epsilon,mu):
        return np.dot((C*np.eye(num) - diag(alpha)),epsilon) - mu
    def make_r_4(alpha,s,mu):
        return np.dot(diag(alpha),s) - mu

    def make_W(alpha):
        W = np.zeros((1,alpha.shape[1]))
        for i in range(num):
            W = W + alpha[i]*Y[i]*X[i,:]
        return W
    def make_b(alpha):
        n_b = 0
        sumA = 0
        sumB = 0
        for i in range(num):
            if alpha[i] > 0 and alpha[i] < C:
                for j in range(num):
                    sumA = sumA + alpha[j]*Y[j]*X[j,:]
                sumB = sumB + Y[i] - np.dot(sumA,X[i,:].T)
                n_b = n_b + 1
        b = sumB/n_b
        return b

    # make initial value
    alpha = np.zeros((num,1))+1e-6
    b = np.mean(Y)
    epsilon = np.zeros((num,1))+1e-6
    s = np.zeros((num,1))
    for i in range(num):
        s[i] = 1 - Y[i]*b
    mu = 3

    for ite_a in range(100):

        for ite_b in range(100):

            r_1 = make_r_1(alpha,b,epsilon,s)
            r_2 = make_r_2(alpha)
            r_3 = make_r_3(alpha,epsilon,mu)
            r_4 = make_r_4(alpha,s,mu)
            KKT = max(abs(r_1).max(),abs(r_2),abs(r_3).max(),abs(r_4).max())

            if ite_b%100 == 0 and ite_b != 0:
                print('iteration in Newton method : %s\n'%ite_b)
                print('max update : %s'%max_update)
                print('max KKT :  %s'%KKT)
            if KKT < convage:
                print('Newton method is convaged   KKT : %s'%KKT)
                break


            Hessian = np.zeros((3*num+1,3*num+1))
            Hessian[0:num,0:num] = Q
            Hessian[num,0:num] = Y.T
            Hessian[num+1:2*num+1,0:num] = diag(epsilon)
            Hessian[2*num+1:3*num+1,0:num] = diag(s)
            Hessian[0:num,num:num+1] = Y
            Hessian[0:num,num+1:2*num+1] = np.eye(num)
            Hessian[num+1:2*num+1,num+1:2*num+1] = diag(C-alpha)
            Hessian[0:num,2*num+1:3*num+1] = -1*np.eye(num)
            Hessian[2*num+1:3*num+1,2*num+1:3*num+1] = diag(alpha)

            RHS = np.zeros((3*num+1,1))
            RHS[0:num] = r_1
            RHS[num] = r_2
            RHS[num+1:2*num+1] = r_3
            RHS[2*num+1:3*num+1] = r_4

            est = np.linalg.solve(Hessian,-RHS)

            update_alpha = est[0:num]
            update_b = est[num]
            update_epsilon = est[num+1:2*num+1]
            update_s = est[2*num+1:3*num+1]

            # decide width by line search

            width = 0.9
            YES = 0
            for i in range(21):
                YES = 0
                if np.all(0<alpha + width*update_alpha) == True:
                    YES = YES + 1
                if np.all(alpha + width*update_alpha<C) == True:
                    YES = YES + 1
                if np.all(0<epsilon+width*update_epsilon) == True:
                    YES = YES +  1
                if np.all(0<s+width*update_s) == True:
                    YES = YES + 1
                if YES == 4:
                    break
                else:
                    width = width/2
            # update
            alpha = alpha + width*update_alpha
            b = b + width*update_b
            epsilon = epsilon + width*update_epsilon
            s = s + width*update_s


            max_update = max(abs(width*update_alpha).max(),abs(update_b).max(),abs(width*update_epsilon).max(),abs(width*update_s).max())
            if max_update < 1e-8:
                print('update is less tha 1e-8, thus Newton method finish\n')
                break

        r_3_LHS = r_3+mu
        r_4_LHS = r_4+mu
        mu_0 = (sum(r_3_LHS)+sum(r_4_LHS))/(2*num)
        new_mu = mu_0*(((1-width)/(10+width))**2)

        print('Now, mu is updated  :  %s'%new_mu)
        if new_mu < convage:
            print('mu is convaged!\n')
            break
        elif abs(new_mu-mu) < 1e-6:
            print('mu is convaged, but mu is : %s'%new_mu)
            break
        else:
            mu = new_mu

    W = make_W(alpha)
    #b = make_b(alpha)
    pdb.set_trace()
    return W,b



class SVM:
    def __init__(self,tra_d,tra_r):
        self.tra_d = tra_d;
        self.tra_r = tra_r;

    def fit(self):
        num = self.tra_d.shape[0]
        dim = self.tra_d.shape[1]
        print('Which do you choice kernel name? (liner or polynomial or RBF)\n')
        kernel_name = input('kernel name :  ')
        if kernel_name == 'liner':
            def K(i,j):
                k = np.dot(self.tra_d[i],self.tra_d[j].T)
                return k
        elif kernel_name == 'polynomial':
            c = float(input('Please c in positive Real number   :'))
            d = int(input('Please d in Natural number  :'))
            def K(i,j):
                k = (np.dot(self.tra_d[i],self.tra_d[j])+c)**d
                return k
        elif kernel_name == 'RBF':
            gamma = float(input('Please gamma in positive Real numver  :'))
            def K(i,j):
                k = np.exp(-gamma*sum((self.tra_d[i]-self.tra_d[j])**2))
                return k

        C = float(input('Regularization parameter  :'))

        Optimize = input('which do you use Optimization (only IPM) : ')
        if Optimize == 'IPM':
            W,b = IPM(self.tra_d,self.tra_r,K,C)


        def D_function(x):
            D = np.dot(W,x.T) + b
            return D

        print('fitting is complicated!\n')

        return D_function, W, b, C,kernel_name


    def predict(self,D_function,tes_d):
        pre = np.zeros((tes_d.shape[0],1))
        for i in range(tes_d.shape[0]):
            P = D_function(tes_d[i,:])
            if P > 0 :
                pre[i] = 1
            if P < 0 :
                pre[i] = -1

        display = input('Do you see predict? (YES or NO)  :')
        if display == 'YES':
            print('OK !!!\n')
            pre_list = pre.tolist()
            result = pd.DataFrame({'predict':pre_list})
            print(result)
        return pre

    def check(self,predict,tes_r):
        rate = 0
        for i in range(tes_r.shape[0]):
            if tes_r[i] == predict[i]:
                rate = rate + 1

        rate = rate/tes_r.shape[0]

        display = input('Do you see result of test? (YES or NO)  :')
        if display == 'YES':
            print('OK !!!\n')
            pre_list = predict.tolist()
            tes_r_list = tes_r.tolist()
            result = pd.DataFrame({'Predict':pre_list,'Correct':tes_r_list})
            print(result)

        print('Percenrage of correct answer : %s'%rate)
        return rate
