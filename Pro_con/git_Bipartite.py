import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class bipartite_judge:
    def __init__(self,network):
        self.network = network
        self.color_r = np.zeros(len(network))


    def judge(self):

        fig = plt.figure()
        ims = []
        self.color_r[0] = 1
        old_node = 0
        def depth(old_node,node):
            C = self.color_r[old_node]
            self.color_r[node] = -C
            for l in self.network[node]:
                if self.color_r[l] == -C:
                    print('this graph is not bipartite')
                    break

            im = plt.bar(range(len(self.color_r)), self.color_r, width=0.5,color='black')
            ims.append(im)

            for adj in self.network[node]:
                if self.color_r[adj] == 0:
                    depth(node,adj)
        node = min(self.network[old_node])
        depth(old_node,node)


        ani = animation.ArtistAnimation(fig, ims, interval=500)
        ani.save("../../dataset/implementation/pro_con/bipatite.gif", writer="imagemagick")


    def add_node(self,adj_node):
        N = len(self.network)
        self.network[N+1] = adj_node
        for i in adj_node:
            self.network[i] = self.network + N+1


def main():

    network = {0:[1,3],1:[0,2],2:[1,3,4],3:[0,2],4:[2]}
    print(network)

    bipar = bipartite_judge(network)
    bipar.judge()
    print(bipar.color_r)

if __name__ == '__main__':
    main()
