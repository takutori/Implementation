import numpy as np
import random
import pdb


class heap_struct:
    def __init__(self):
        self.heap = np.array([])
        self.num = 0


    def add(self,x):
        self.heap = np.insert(self.heap,self.num,x)
        sz = self.num
        self.num = self.num + 1

        for i in range(10000):
            if sz == 0:
                par = 0
            if sz%2 == 0 and sz != 0:
                par = int((sz-2)/2)
            elif sz%2 == 1 and sz != 0:
                par = int((sz-1)/2)

            if self.heap[sz] < self.heap[par]:
                out_box = self.heap[par]
                self.heap[par] = self.heap[sz]
                self.heap[sz] = out_box
                sz = int(par)
            else:
                break

    def pick(self):
        y = self.heap[0] #根の値を取り出す。
        self.heap[0] = self.heap[self.num-1] #一番下のnodeの値を根にコピー
        self.heap = np.delete(self.heap,self.num-1,axis=0) #一番最後のnodeを削除
        self.num = self.num-1 #node数が一つ減る
        sz = 0
        for i in range(10000):

            if sz*2+1 >= self.num-1 or self.num-1 == 0:
                break

            if self.heap[sz*2+1] > self.heap[sz*2+2]:
                week_point = sz*2+2
                week_par = self.heap[sz*2+2]
            elif self.heap[sz*2+1] < self.heap[sz*2+2]:
                week_point = sz*2+1
                week_par = self.heap[sz*2+1]
            if self.heap[sz] > week_par:
                out_box = week_par
                self.heap[week_point] = self.heap[sz]
                self.heap[sz] = out_box
                sz = week_point
            else:
                break
        return y


def heap_sort(X):

    heap_arr = heap_struct()
    sort_X = np.array([])
    # heap構造に追加
    for i in range(len(X)):
        heap_arr.add(X[i])

    # heap構造から抽出
    for i in range(len(X)):
        y = heap_arr.pick()
        sort_X = np.insert(sort_X,i,y)

    return sort_X

def main():

    X = np.array([random.randrange(100) for i in range(10)])
    sort_ru = heap_sort(X)
    print(X)
    print(sort_ru)


if __name__ == '__main__':
    main()
