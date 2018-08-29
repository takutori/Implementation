import numpy as np


def main():

    X = int(input('Natural number :'))
    d = 2
    while d*d <= X:
        if X%d == 0:
            X = X/d
            print('%s * '%d)
        else:
            d = d + 1
    print('%s \n'%X)



if __name__ == '__main__':
    main()
