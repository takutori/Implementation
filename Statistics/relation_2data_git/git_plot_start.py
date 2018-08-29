import sys
import os
import parser
import argparse
import os
import numpy as np
from tra_scatter import cal_w
from tra_scatter import gausu_double
from tra_scatter import bef_afscatter

parser = argparse.ArgumentParser(description = 'data loading trial')
parser.add_argument('--filename','-data',type=str,default='piyo',help='filename in dataset folder')

args = parser.parse_args()
filename = args.filename
filepath = os.path.join('../../dataset/py_study/','%s.npy'%filename)
filearray = np.load(filepath)


def main():
    w = cal_w(filearray)
    print('download data which arraysize is 2 x 1000 in gausu_normal\n and display transformed data ')
    gausu_normal = gausu_double()
    data = np.dot(w,gausu_normal.T)
    print('transformed data = %s\n \n'%data)
    bef_afscatter(data,filearray)
    print('computation sequence of methed plot_start completed! \n \nplease check your datasetfile')

if __name__ == '__main__':
 main()
