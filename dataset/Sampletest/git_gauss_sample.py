import numpy as np


def two_class():

    d_num_1 = int(input('number of class C_1 of training data :'))
    d_num_2 = int(input('number of class C_2 of training data :'))
    dim = int(input('dimention  :'))
    ML_name = input('Which do you choice (SVM or Logistic)?')
    if ML_name == 'SVM':
        C_value = -1
    if ML_name == 'Logistic':
        C_value = 0

    X_1 = np.random.randn(d_num_1,dim)
    X_2 = np.random.randn(d_num_2,dim)*5+10
    X_d = np.concatenate([X_1,X_2],axis=0)

    xx_1 = np.ones((d_num_1,1))
    xx_2 = np.ones((d_num_2,1))*C_value
    X_r = np.concatenate([xx_1,xx_2],axis=0)


    t_num_1 = int(input('number of class C_1 of test data :'))
    t_num_2 = int(input('number of class C_2 of test data :'))

    Y_1 = np.random.randn(t_num_1,dim)
    Y_2 = np.random.randn(t_num_2,dim)*5+10
    Y_d = np.concatenate([Y_1,Y_2],axis=0)

    yy_1 = np.ones((t_num_1,1))
    yy_2 = np.ones((t_num_2,1))*C_value
    Y_r = np.concatenate([yy_1,yy_2],axis=0)

    np.save('Implementation/Sampletest/training_data',X_d)
    np.save('Implementation/Sampletest/training_r',X_r)
    np.save('Implementation/Sampletest/test_data',Y_d)
    np.save('Implementation/Sampletest/test_r',Y_r)


    print('Saving training data and test data is complicated!\n')
    print('training data have difference of 0.5 between C_1 and C_2\n ')
    print('test data consist of 100 samples. \n if you want to test more sample number, change this code in dataset/implementation/Sampletest/gauss_sample.py')
