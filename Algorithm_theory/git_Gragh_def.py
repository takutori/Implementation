import numpy as np





class directed_Gragh():
    def __init__(self,E,V,gragh_map):
        self.edge = E;
        self.vertex = V;
        self.map = gragh_map;

    def Adjacency_matrix(self):
        adjacency_matrix = np.zeros((self.vertex.shape[0],self.vertex.shape[0]))
        for ed in self.edge:
            P_ = self.map(ed)
            start = P_[0]
            end = P_[1]
            row = np.where(self.vertex == start)
            column = np.where(self.vertex == end)
            adjacency_matrix[row,column] = 1
            adjacency_matrix[column,row] = 1
        return adjacency_matrix
