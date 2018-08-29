import numpy as np
import sys
import os
from SVM_def import SVM


tra_d = np.load('../../dataset/implementation/svm/svm_tra_d.npy')
tra_r = np.load('../../dataset/implementation/svm/svm_tra_r.npy')
tes_d = np.load('../../dataset/implementation/svm/svm_tes_d.npy')
tes_r = np.load('../../dataset/implementation/svm/svm_tes_r.npy')


def main():

    print('Start SVM algorithm\n')
    test = SVM(tra_d,tra_r)
    f = test.fit()
    predict = test.predict(f,tes_d)
    rate = test.check(predict,tes_r)
    print('Algorithm is finished\n')

if __name__ == '__main__':
    main()
