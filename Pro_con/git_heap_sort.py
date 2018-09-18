import numpy as np
from heap import heap_struct
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def heap_sort(X):

    fig = plt.figure()
    ims = []
    ims2 = []

    #im = plt.bar(range(len(X)), X, width=0.5,color='black',tick_label='初期配列')
    #ims.append(im)

    heap_arr = heap_struct()
    sort_X = []
    # heap構造に追加
    for i in range(len(X)):
        heap_arr.add(X[i])
        im = plt.bar(range(heap_arr.num), heap_arr.heap, width=0.5,color='black',tick_label='ヒープ構造へ...')
        ims2.append(im)

    # heap構造から抽出
    for i in range(len(X)):
        y = heap_arr.pick()
        sort_X.append(y)

        im = plt.bar(range(len(heap_arr.heap)),heap_arr.heap, width=0.5,color='black',tick_label='sort中...')
        ims2.append(im)
        #im = plt.bar(range(len(sort_X)),sort_X, width=0.5,color='black',tick_label='sort中...')
        #ims.append(im)                  # グラフを配列 ims に追加


    #ani = animation.ArtistAnimation(fig, ims, interval=100)
    ani2 = animation.ArtistAnimation(fig,ims2,interval=500)
    ani2.save("../../dataset/implementation/pro_con/heap_add_pick.gif", writer="imagemagick")

    return np.array(sort_X)



def main():

    X = np.array([random.randrange(100) for i in range(10)])
    sort_ru = heap_sort(X)
    print(X)
    print(sort_ru)


if __name__ == '__main__':
    main()
