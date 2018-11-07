import numpy as np
import matplotlib.pyplot as plt
from reg_def import polynomial_fit
import pdb

import parser
import argparse
import os
parser = argparse.ArgumentParser(description='parameter alpha')
parser.add_argument('--xfile','-xf',type=str,default='piyo',help='filename in dataset folder')
parser.add_argument('--yfile','-yf',type=str,default='piyo',help='filename in dataset folder')
parser.add_argument('--order', '-M', type=int, default=5,help='filename in dataset folder')
parser.add_argument('--alpha', '-alpha', type=float, default=1.0,help='filename in dataset folder')
parser.add_argument('--beta', '-beta', type=float, default=1.0,help='filename in dataset folder')
args = parser.parse_args()
order = args.order
p_alpha = args.alpha
p_beta = args.beta
X_file = args.xfile
Y_file = args.yfile
train_x = np.load('../../../dataset/implementation/ML/Regression/{}'.format(X_file))
train_y = np.load('../../../dataset/implementation/ML/Regression/{}'.format(Y_file))




def main():
    x = 3
    pdb.set_trace()

    test = polynomial_fit(train_x,train_y)
    test.Bayesian_fit(M = order,alpha=p_alpha,beta=p_beta)
    test.plot(filename=X_file)



if __name__ == '__main__':
    main()
