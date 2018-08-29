import numpy as np
import sys
import os

from Logistic_def import Logistic


tra_d = np.load('../../dataset/implementation/Occupancy_data/mini_log_tra_d.npy')
tra_r = np.load('../../dataset/implementation/Occupancy_data/mini_log_tra_r.npy')
tes_d = np.load('../../dataset/implementation/Occupancy_data/mini_log_tes_d.npy')
tes_r = np.load('../../dataset/implementation/Occupancy_data/mini_log_tes_r.npy')



def main():
    print('Start Logistic Regression\n')
    Logistic_model = Logistic(tra_d,tra_r)
    decition_func = Logistic_model.fit()
    P,predict = Logistic_model.predict(tes_d,decition_func)
    rate = Logistic_model.check(P,predict,tes_r)


if __name__ == '__main__':
    main()
