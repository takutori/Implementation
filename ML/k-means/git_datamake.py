import numpy as np
import matplotlib.pyplot as plt
import pdb

def circle():
    num = 300
    dim = 2

    # データ点のために乱数列を固定
    np.random.seed(0)

    data = np.zeros((num,dim))
    classter = np.zeros((num,1)).reshape(num,)
    theta_1 = (2*np.pi)/100
    theta_2 = (2*np.pi)/200

    for i in range(num):
        if i <= 100:
            x_1 = 0.5*np.sin(theta_1*i)+0.5*np.random.randn()
            y_1 = 0.5*np.cos(theta_1*i)+0.5*np.random.randn()
            data[i,0] = x_1
            data[i,1] = y_1
            classter[i] = 1
        else:
            x_2 = 10*np.sin(theta_2*(i-100))+0.5*np.random.randn()
            y_2 = 10*np.cos(theta_2*(i-100))+0.5*np.random.randn()
            data[i,0] = x_2
            data[i,1] = y_2
            classter[i] = 2
    plt.scatter(data[:,0],data[:,1],s=10,marker='x')
    plt.title('ANSWER CLUSSTERING')
    plt.savefig('image/answer_circledata_clusttering.png')

    np.save('data/circle_data',data)

    print('Saving training data and test data is complicated!\n')
    print('test data consist of %s samples. \n if you want to test more sample number, change this code in dataset/implementation/k-means/datamake.py'%num)

def normal():
    dim = 2
    class_1 = -1*np.random.randn(100,dim)-10
    classter_1 = np.ones((100,1))

    class_2 = -1*np.random.randn(100,dim)-10
    class_2[:,0] = class_2[:,0] + 10
    classter_2 = np.ones((100,1))+1

    class_3 = np.random.randn(100,dim)-10
    class_3[:,0] = class_3[:,0] + 5
    class_3[:,1] = class_3[:,1] + 5
    classter_3 = np.ones((100,1))+2
    data  = np.concatenate((class_1,class_2),axis=0)
    data = np.concatenate((data,class_3),axis=0)
    classter = np.concatenate((classter_1,classter_2),axis=0)
    classter = np.concatenate((classter,classter_3),axis=0)
    classter = classter.reshape(classter.shape[0],)

    plt.scatter(data[:,0],data[:,1],s=10,marker='x')
    plt.title('ANSWER CLUSSTERING')
    plt.savefig('image/answer_randomdata_clusttering.png')

    np.save('data/random_data',data)
    num = data.shape[0]
    print('Saving training data and test data is complicated!\n')
    print('test data consist of %s samples. \n if you want to test more sample number, change this code in dataset/implementation/k-means/datamake.py'%num)



def main():
    dataname = input('data name (circle,random)  :')
    if dataname == 'circle':
        circle()
    if dataname == 'random':
        normal()
    else:
        print('THIS DATA IS NOT EXISTS')

if __name__ == '__main__':
    main()
