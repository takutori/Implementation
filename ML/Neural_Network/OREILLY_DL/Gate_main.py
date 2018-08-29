from Gate import AND,NAND,OR,XOR
import numpy as np






def main():
    print('please 1 or 0')
    x_1 = int(input('x_1 = :'))
    x_2 = int(input('x_2 = :'))
    X = np.array([x_1,x_2])


    print('AND Gate: %s'%AND(X))
    print('NAND Gate: %s'%NAND(X))
    print('OR Gate: %s'%OR(X))
    print('XOR Gate: %s'%XOR(X))

if __name__ == '__main__':
    main()
