import numpy as np
import parser
import argparse
import os
from SNE_def import SNE
import pdb
parser = argparse.ArgumentParser(description='data loading trial')
parser.add_argument('--filename', '-f', type=str, default='piyo',
                    help='filename in dataset folder')
args = parser.parse_args()
filename = args.filename
filepath = os.path.join('../../dataset/gene/', '%s'%filename)
filearray = np.load(filepath)

def main():

    X = filearray


    Expeliment = SNE(X)

    Expeliment.plot(filename)

if __name__ == '__main__':
    main()



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
