import numpy as np
import random
import pdb


class heap_struct:
    def __init__(self):
        self.heap = []
        self.num = 0

    """
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
    """

    def add(self,x,node_name):
        self.heap.append(node_name+'='+str(x))
        sz = len(self.heap)-1

        for i in range(10000):
            if sz == 0:
                par = 0
            elif sz%2 == 0:
                par = int((sz-2)/2)
            elif sz%2 == 1:
                par = int((sz-1)/2)

            heap_sz = float(self.heap[sz].split('=')[1])
            heap_par = float(self.heap[par].split('=')[1])
            if heap_sz < heap_par:
                out_box = self.heap[par]
                self.heap[par] = self.heap[sz]
                self.heap[sz] = out_box
                sz = int(par)
            else:
                break

    """
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

    """


    def pick(self):
        root_node_name = self.heap[0] #根の値を取り出す。
        self.heap[0] = self.heap[len(self.heap)-1] #一番下のnodeの値を根にコピー
        del self.heap[len(self.heap)-1] #一番最後のnodeを削除
        sz = 0
        for i in range(10000):

            if sz*2+1 >= len(self.heap)-1 or len(self.heap)-1 == 0:
                break

            heap_sz = float(self.heap[sz].split('=')[1])
            heap_sz_1 = float(self.heap[sz*2+1].split('=')[1])
            heap_sz_2 = float(self.heap[sz*2+2].split('=')[1])

            if heap_sz_1 >= heap_sz_2:
                child_index = sz*2+2
                week_child = heap_sz_2
            elif heap_sz_1 < heap_sz_2:
                child_index = sz*2+1
                week_child = heap_sz_1
            else:
                print('error')

            if heap_sz > week_child:
                out_box = self.heap[sz]
                self.heap[sz] = self.heap[child_index]
                self.heap[child_index] = out_box
                sz = child_index
            else:
                break
        return float(root_node_name.split('=')[1]),root_node_name.split('=')[0]


    def change(self,value,node_name):
        for i in range(len(self.heap)):
            ch_name = self.heap[i].split('=')[0]
            if ch_name == node_name:
                self.heap[i] = ch_name + '=' + str(value)
                sz_sz = i

        #ヒープ構造を保つように上へ上げていく
        for i in range(10000):
            if sz_sz == 0:
                par = 0
            if sz_sz%2 == 0 and sz_sz != 0:
                par = int((sz_sz-2)/2)
            elif sz_sz%2 == 1 and sz_sz != 0:
                par = int((sz_sz-1)/2)

            heap_par = float(self.heap[par].split('=')[1])
            if value < heap_par:
                out_box = self.heap[par]
                self.heap[par] = self.heap[sz_sz]
                self.heap[sz_sz] = out_box
                sz_sz = int(par)

            else:
                break


    def pick_value(self,node_name):
        #pdb.set_trace()
        res = 'not found'
        for i in range(len(self.heap)):
            pick = self.heap[i].split('=')[0]
            if node_name == pick:
                res = float(self.heap[i].split('=')[1])
        if res == 'not found':
            print('not found')
        return res

def main():

    X = np.array([random.randrange(10) for i in range(10)])
    heap_arr = heap_struct()
    for i in range(len(X)):
        heap_arr.add(X[i],str(i))

    print(heap_arr.heap)
    pdb.set_trace()
    x = heap_arr.pick()
    pdb.set_trace()



    print(heap_arr.heap)
if __name__ == '__main__':
    main()
