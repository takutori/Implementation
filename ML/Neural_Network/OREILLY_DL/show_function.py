import numpy as np
import matplotlib.pyplot as plt

from activ_function import step_func,sigmoid,ReLU,softmax


def main():

    range_1 = int(input('left of X range :'))
    range_2 = int(input('right of X range :'))

    x = np.arange(range_1,range_2,0.1)

    func_name = input('function name (step,sigmoid,softmax,ReLU)  :')

    if func_name == 'step':
        y = step_func(x)
    elif func_name == 'sigmoid':
        y = sigmoid(x)
    elif func_name == 'ReLU':
        y = ReLU(x)
    elif func_name == 'softmax':
        y = softmax(x)

    image_name = func_name + 'png'
    plt.plot(x,y)
    plt.ylim(-0.1,1.1)
    plt.show()
    plt.savefig('../../../../dataset/implementation/NuralNetwork/%s'%image_name)

if __name__ == '__main__':
    main()
