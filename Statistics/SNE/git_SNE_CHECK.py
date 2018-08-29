import numpy as np
import matplotlib.pyplot as plot
import sys
import os
from SNE_def import SNE

def main():

    data = np.random.randn(3,3)

    Expeliment = SNE(data)
    embed = Expeliment.plot('SNE_CHECK')

    AB = np.linalg.norm(data[0,:]-data[1,:])
    BC = np.linalg.norm(data[1,:]-data[2,:])
    CA = np.linalg.norm(data[2,:]-data[0,:])

    e_AB = np.linalg.norm(embed[0,:]-embed[1,:])
    e_BC = np.linalg.norm(embed[1,:]-embed[2,:])
    e_CA = np.linalg.norm(embed[2,:]-embed[0,:])

    print('before data\n')
    print('AB = {}, BC = {}, CA = {}'.format(AB,BC,CA))
    print('embeded data\n')
    print('e_AB = {}, e_BC = {}, e_CA = {}'.format(e_AB,e_BC,e_CA))

if __name__ == '__main__':
    main()
