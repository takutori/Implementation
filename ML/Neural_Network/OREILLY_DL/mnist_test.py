import sys, os
import numpy as np
sys.path.append('C:\\Users\\Taniguchi\\Desktop\\Programing\\dataset\\Implementation\\NuralNetwork\\OREILLY_ML')
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

def main():

    (x_train,t_train),(x_test,t_test) = load_mnist(flatten=True,normalize=False)
    img = x_train[0]
    label = t_train[0]
    print('label : %s'%label)
    img = img.reshape(28,28)
    shape_1 = img.shape[0]
    shape_2 = img.shape[1]
    print('shape : {} * {}'.format(shape_1,shape_2))

    print('show image')
    img_show(img)

if __name__ == '__main__':
    main()
