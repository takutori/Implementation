import numpy as np
import pdb

def step_func(x):
    return np.array(x>0,dtype=np.int)


def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(x):
    c = np.max(x)
    exp_x = np.exp(x-c)
    sum_exp_x = np.sum(exp_x)
    y = exp_x / sum_exp_x
    return y

def ReLU(x):
    return np.maximum(0,x)
