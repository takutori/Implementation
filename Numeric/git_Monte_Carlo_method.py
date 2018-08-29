import numpy as np


def main():
    c = 0
    for i in range(10000):
        x = np.random.rand()
        y = np.random.rand()

        if x <= 1:
            if y <= 1 - x:
                c = c + 1

    print(c/10000)


if __name__ == '__main__':
    main()
