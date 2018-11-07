import numpy as np


def samplesin(X):
    return np.sin(X)


def main():

    sampleN = int(input('sample number: '))
    modelname = input('model name (sin): ')
    import pdb;pdb.set_trace()
    X_axis = np.arange(0,2*np.pi,2*np.pi/sampleN)
    ran = 0.3*np.random.randn(sampleN)
    if modelname == 'sin':
        train_d_set = samplesin(X_axis)+ran
    else:
        print('not exists model name')

    np.save('objective_data_sample-{}_modelname-{}'.format(sampleN,modelname),X_axis)
    np.save('target_datasample-{}_modelname-{}'.format(sampleN,modelname),train_d_set)
if __name__ == '__main__':
    main()
