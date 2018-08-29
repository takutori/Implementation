import numpy as np
from kernel_Kmeans_def import k_means
from kernel_Kmeans_def import plot_classtering
import parser
import argparse
import os
parser = argparse.ArgumentParser(description='data loading trial')
parser.add_argument('--filename', '-f', type=str, default='piyo',
                    help='filename in dataset folder')
args = parser.parse_args()
filename = args.filename
filepath = os.path.join('../../dataset/implementation/k-means/data', '%s.npy'%filename)
dataset = np.load(filepath)

def make_kernel(name):
    if name == 'linear':
        def kernel(x,y):
            K = np.dot(x,y)
            return K
    elif name == 'RBF':
        gamma = float(input('gamma (positive real number)  :'))
        def kernel(x,y):
            K = np.exp(-gamma*(sum((x-y)**2)))
            return K
    elif name == 'Polynomial':
        c = float(input('c (positive real number)  :'))
        d = int(input('d (natural numver)  :'))
        def kernel(x,y):
            K = (np.dot(x.T,y)+c)**d
            return K
    else:
        print('THIS KERNEL IS NOT EXIST\n')

    return kernel

def main():
    k_name = input('kernel name (linear,RBF,polynomial) :')
    kernel = make_kernel(k_name)

    K = int(input('clustering number : '))
    classter = k_means(dataset,K,kernel)

    savedataname = 'classter' + filename + 'k_name'
    np.save('../../dataset/implementation/k-means/data/classter_%s'%savedataname,classter)
    print('saving clusster is complicated!')

    plot_classtering(dataset,classter,K,filename,k_name)

if __name__ == '__main__':
    main()
