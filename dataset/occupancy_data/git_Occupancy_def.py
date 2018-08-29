import numpy as np
import pandas as pd


def Occupancy_set():
    print('get occupancy data\n')
    datatest = pd.read_table('C:/Users/Taniguchi/Desktop/dataset/implementation/occupancy_data/datatest.txt',sep=',')
    datatest2 = pd.read_table('C:/Users/Taniguchi/Desktop/dataset/implementation/occupancy_data/datatest2.txt',sep=',')
    datatraining = pd.read_table('C:/Users/Taniguchi/Desktop/dataset/implementation/occupancy_data/datatraining.txt',sep=',')
    n_datatraining = np.array(datatraining)
    n_datatest = np.concatenate([np.array(datatest),np.array(datatest2)],axis=0)

    print('changing date data into int data')
    for i in range(n_datatraining.shape[0]):
        year,manth,day_time = n_datatraining[i,0].split('-')
        day,time = day_time.split(' ')
        hour,minuts,second = time.split(':')
        n_datatraining[i,0] = int(year+manth+day+hour+minuts+second)

    for i in range(n_datatest.shape[0]):
        year,manth,day_time = n_datatest[i,0].split('-')
        day,time = day_time.split(' ')
        hour,minuts,second = time.split(':')
        n_datatest[i,0] = int(year+manth+day+hour+minuts+second)

    ML_name = input('which is ML name SVM or Logistic?  :')
    if ML_name == 'SVM':
        print('Ok, changeing data for SVM\n')
        svm_tra = n_datatraining
        svm_tes = n_datatest
        for i in range(svm_tra.shape[0]):
            if svm_tra[i,6] == 0:
                svm_tra[i,6] = -1
        for j in range(svm_tes.shape[0]):
            if svm_tes[j,6] == 0:
                svm_tes[j,6] = -1
        svm_tra[:,0] = (svm_tra[:,0]-np.mean(svm_tra[:,0]))/np.std(svm_tra[:,0])
        svm_tes[:,0] = (svm_tes[:,0]-np.mean(svm_tes[:,0]))/np.std(svm_tes[:,0])

        d_num = int(input('trainig data size :'))
        t_num = int(input('test data size :'))

        mini_svm_tra_d = np.zeros((d_num,6))
        mini_svm_tra_r = np.zeros((d_num,1))
        mini_svm_tes_d = np.zeros((t_num,6))
        mini_svm_tes_r = np.zeros((t_num,1))
        for i in range(d_num):
            index = np.random.randint(0,svm_tra.shape[0])
            mini_svm_tra_d[i,0:6] = svm_tra[index,0:6]
            mini_svm_tra_r[i,0] = svm_tra[index,6]
        for j in range(t_num):
            index = np.random.randint(0,svm_tes.shape[0])
            mini_svm_tes_d[j,0:6] = svm_tes[index,0:6]
            mini_svm_tes_r[j,0] = svm_tes[index,6]

        np.save('C:/Users/Taniguchi/Desktop/dataset/implementation/svm/svm_tra_d',mini_svm_tra_d)
        np.save('C:/Users/Taniguchi/Desktop/dataset/implementation/svm/svm_tra_r',mini_svm_tra_r)
        np.save('C:/Users/Taniguchi/Desktop/dataset/implementation/svm/svm_tes_d',mini_svm_tes_d)
        np.save('C:/Users/Taniguchi/Desktop/dataset/implementation/svm/svm_tes_r',mini_svm_tes_r)

    if ML_name == 'Logistic':
        print('Ok,changing data for Logistic\n')
        log_tra = n_datatraining
        log_tes = n_datatest
        d_num = int(input('datatraining data size :'))
        t_num = int(input('test data size :'))
        mini_log_tra_d = np.zeros((d_num,6))
        mini_log_tra_r = np.zeros((d_num,1))
        mini_log_tes_d = np.zeros((t_num,6))
        mini_log_tes_r = np.zeros((t_num,1))
        for i in range(d_num):
            d_index = np.random.randint(0,log_tra.shape[0])
            mini_log_tra_d[i,0:6] = log_tra[d_index,0:6]
            mini_log_tra_r[i,0] = log_tra[d_index,6]
        for j in range(t_num):
            t_index = np.random.randint(0,log_tes.shape[0])
            mini_log_tes_d[j,0:6] = log_tes[t_index,0:6]
            mini_log_tes_r[j,0] = log_tes[t_index,6]

        mini_log_tra_d[:,0] = (mini_log_tra_d[:,0] - np.mean(mini_log_tra_d[:,0]))/np.std(mini_log_tra_d[:,0])
        mini_log_tes_d[:,0] = (mini_log_tes_d[:,0] - np.mean(mini_log_tes_d[:,0]))/np.std(mini_log_tes_d[:,0])
        np.save('C:/Users/Taniguchi/Desktop/dataset/implementation/Logistic/log_tra_d',mini_log_tra_d)
        np.save('C:/Users/Taniguchi/Desktop/dataset/implementation/Logistic/log_tra_r',mini_log_tra_r)
        np.save('C:/Users/Taniguchi/Desktop/dataset/implementation/Logistic/log_tes_d',mini_log_tes_d)
        np.save('C:/Users/Taniguchi/Desktop/dataset/implementation/Logistic/log_tes_r',mini_log_tes_r)

    print('Ok, preprocessing is complicated!\n')
