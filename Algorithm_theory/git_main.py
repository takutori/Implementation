
import numpy as np
from Gragh_def import directed_Gragh


def main():

    vertex = np.array(['house','station','school','hospital'])
    edge = np.array([1,2,3,4])

    def gragh_map(edge):
        if edge == 1:
            vertexs = np.array(['house','school'])
        elif edge == 2:
            vertexs = np.array(['school','station'])
        elif edge == 3:
            vertexs = np.array(['house','station'])
        else:
            vertexs = np.array(['station','hospital'])
        return vertexs

    test_gragh = directed_Gragh(edge,vertex,gragh_map)
    print('vertex is %s \n'%test_gragh.vertex)

    adjacency_matrix = test_gragh.Adjacency_matrix()

    print('adjacency_matrix = \n %s \n'%adjacency_matrix)

if __name__ == '__main__':
        main()
