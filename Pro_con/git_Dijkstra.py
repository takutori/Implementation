import numpy as np
import random
from heap import heap_struct
import pdb
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import parser
import argparse
import os
parser = argparse.ArgumentParser(description='node number')
parser.add_argument('--node_num', '-n', type=int, default=10,
                    help='filename in dataset folder')
args = parser.parse_args()
node_num = args.node_num


print(node_num)


def dijkstra(network,weght,start,goal):

    fig = plt.figure()
    ims = []


    flag = []
    d_goal = [10000 for i in range(len(network))]

    im = plt.bar(range(len(d_goal)),d_goal,width=0.5,color='black')
    plt.ylim(ymax = 230,ymin=0)
    ims.append(im)

    d = heap_struct()
    for i in network.keys():
        d.add(1000,str(i))

    node = start #スタート始点のノード
    d.add(0,str(start)) #スタート地点0のdは0
    d_goal[0] = 0

    im = plt.bar(range(len(d_goal)),d_goal,width=0.5,color='black')
    plt.ylim(ymax = 230,ymin=0)
    ims.append(im)

    for iter in range(10000):

        d_min,min_name = d.pick()
        if min_name not in flag:
            #d_goal[int(min_name)] = d_min
            adj = network[int(min_name)] #隣接ノード

            for tar_adj in adj:
                index_tar_adj = adj.index(tar_adj)
                #pdb.set_trace()
                dist = d_min+weght[int(min_name)][index_tar_adj]
                if d_goal[tar_adj] > dist:
                    #pdb.set_trace()
                    d_goal[tar_adj] = dist

                    im = plt.bar(range(len(d_goal)),d_goal,width=0.5,color='black')
                    plt.ylim(ymax = 230,ymin=0)
                    ims.append(im)

                    #print('min_node={}->tar_node={}'.format(min_name,tar_adj))
                    #print('{} * {} = {}'.format(d_min,weght[int(min_name)][index_tar_adj],dist))
                    #print(d_goal)
                    d.add(dist,str(tar_adj))
            #pdb.set_trace()
            #選択されたノードの抹消
            flag.append(min_name)
            print('%s node is complicated!'%len(flag))
            #pdb.set_trace()
            for key in range(len(network)):
                if int(min_name) in network[key]:
                    index_min_name = network[key].index(int(min_name))
                    del network[key][index_min_name]
                    del weght[key][index_min_name]
                    #print(network)
            #print(network)
            #print(weght)

            if len(flag) == len(network):
                print('complicated!')
                break
        else:
            continue

    ani = animation.ArtistAnimation(fig,ims,interval=200)
    ani.save("../../dataset/implementation/pro_con/dijkstra.gif", writer="imagemagick")

    return d_goal





def main():

    #network = {0:[1,2],1:[0,2,3,4],2:[0,1,3],3:[1,2,5],4:[1,5,6],5:[3,4,5],6:[4,5]}
    #weght = {0:[2,5],1:[2,4,6,10],2:[5,4,2],3:[2,6,1],4:[10,3,5],5:[1,3,9],6:[5,9]}


    print('node number is : %s'%node_num)
    print('start to make graph')
    network = {}
    weght = {}
    for node in range(node_num):
        adj_num = int(float(random.randrange(node_num))/3.0)
        network[node] = [random.randrange(node_num) for i in range(adj_num)]
        weght[node] = [random.randrange(100) for i in range(adj_num)]

    print('network = %s'%network)
    print('weght = %s'%weght)

    print('start dijkstra algorithm:')


    print(dijkstra(network,weght,0,4))



if __name__ == '__main__':
    main()
