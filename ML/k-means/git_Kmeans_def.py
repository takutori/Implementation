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
        centroid[0,:] = X[0,:]
        centroid[1,:] = X[120,:]
        centroid[2,:] = X[299,:]
    return centroid



def plot_classtering(X,classter,centroid,dataname,kernel_name):
    color_list = ['red','blue','green','yellow','cyan','magenta']
    for C in range(centroid.shape[0]):
        class_lavel = 'class'+str(C)
        plt.scatter(X[classter==C,0],X[classter==C,1],s=10,marker='x',c=color_list[C],label=class_lavel)
    plt.scatter(centroid[:,0],centroid[:,1],s=10,marker='o',c='black',label='centroid')
    plt.legend()
    plt.title('kernel=%s k-means clustering'%kernel_name)
    plt.savefig('../../dataset/implementation/k-means/image/data={}_kernel={}_k-menas.png'.format(dataname,kernel_name))

def k_means(X,K,kernel):
    print('Start k-means algorithm\n Clustering numver is %s'%K)
    num,dim = X.shape

    old_centroid = intial_centroid(X,K)

    classter = np.zeros((num,1)).reshape(num,)

    for iteration in range(100):

        # clastering
        for n in range(num):
            min_distance = 1e+10
            for c in range(K):
                new_distance = kernel(old_centroid[c,:]-X[n,:],old_centroid[c,:]-X[n,:])
                #new_distance = np.linalg.norm(old_centroid[c,:]-X[n,:])

                if min_distance > new_distance:
                    min_distance = new_distance
                    cla = c
            classter[n] = cla

        # compute mean vector
        new_centroid = np.zeros((K,dim))
        for k in range(K):
            new_centroid[k,:] = np.mean(X[classter==k],axis=0)

        change = (np.linalg.norm(new_centroid - old_centroid,axis=1)).max()


        if iteration == 100 and iteration != 0:
            print("%s's E and M step"%iteration)
            print('centroid change : %s'%change)

        if change < 0.01:
            print('controid is convaged!')
            print('centroid change %s'%change)
            break

    return classter,new_centroid
