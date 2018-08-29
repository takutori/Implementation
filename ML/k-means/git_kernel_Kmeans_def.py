import numpy as np
import matplotlib.pyplot as plt
import pdb

def intial_centroid(X,K):
    centroid_algorithm = input('which do you use method computing initial centroid ?(practice,random)  :')
    if centroid_algorithm == 'random':
        centroid = np.zeros((K,X.shape[1]))
        for i in range(K):
            index = np.random.choice(range(X.shape[0]))
            centroid[i,:] = X[index,:]
    if centroid_algorithm == 'practice':
        centroid = np.zeros((K,X.shape[1]))
        centroid[0,:] = np.aray([0,0])
        centroid[1,:] = np.aray([10,10])
    return centroid



def plot_classtering(X,classter,K,dataname,kernel_name):
    color_list = ['red','blue','green','yellow','cyan','magenta']
    print(classter)
    for C in range(K):
        class_lavel = 'class'+str(C)
        plt.scatter(X[classter==C,0],X[classter==C,1],s=10,marker='x',c=color_list[C],label=class_lavel)

    plt.legend()
    plt.title('kernel=%s k-means clustering'%kernel_name)
    plt.savefig('../../dataset/implementation/k-means/image/data={}_kernel={}_k-menas.png'.format(dataname,kernel_name))

def k_means(X,K,kernel):
    print('Start k-means algorithm\n Clustering numver is %s'%K)
    num,dim = X.shape

    classter = np.zeros((num,1)).reshape(num,)
    for i in range(num):
        classter[i] = np.random.choice(range(K))

    # make kernel gram matrix
    K_gram = np.zeros((num,num))
    for i in range(num):
        for j in range(num):
            K_gram[i,j] = kernel(X[i,:],X[j,:])
    print('kernel gram matrix is maked.')

    for iteration in range(10):

        for i in range(num):#data point fixed
            mindiff = 1e+10
            k_sum1 = 0
            k_sum2 = 0
            for k in range(K):#class fixed
                S = []# make k class point set
                for index in range(num):
                    if classter[index] == k:
                        S.append(index)

                for s in S:
                    k_sum1 = k_sum1 + K_gram[i,s]
                    for t in S:
                        k_sum2 = k_sum2 + K_gram[s,t]

                diff = -1*(2*k_sum1)/len(S) + (k_sum2)/(len(S)**2)

                if mindiff > diff:
                    mindiff = diff
                    classter[i] = k
            #if i%10 == 0:
                #print("{}'points is finished in {}".format(i,iteration))

        if iteration == 10 and iteration != 0:
            print("%s's E and M step"%iteration)

    return classter
