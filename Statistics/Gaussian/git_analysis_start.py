import numpy as np
import sys
import os
import parser
import argparse
import sig_analysis
from sig_analysis import singular_analysis


parser = argparse.ArgumentParser(description = 'data loading trial')
parser.add_argument('--dataname','-data',type = str,default = 'data',
                    help='filename in dataset folder')
args = parser.parse_args()
dataname = args.dataname
datapath = os.path.join('../dataset/py_study/','%s.npy'%dataname)
data = np.load(datapath)

def main():


 print(singular_analysis(data))
 print('computation sequence of method sig_analysis completed!')

if __name__ == '__main__':
 main()
