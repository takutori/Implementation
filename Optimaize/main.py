import numpy as np
from Optimization import Robbins_monro
import sys
sys.path.append('gradient')
from testgrad import function
from testgrad import grad



def main():

    answer = Robbins_monro(function,grad,2)
    print(answer)


if __name__ == '__main__':
        main()
