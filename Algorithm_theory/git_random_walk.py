import numpy as np


def main():

    print('This random walk is :\n 1 - right \n 2 - up \n 3 - left \n 4 - down \n 5 and 6 - stop\n')
    times = int(input('walk times :  '))
    start = np.array([0,0])
    for i in range(times):
        direction = np.random.choice(range(0,6))
        if direction == 1:
            start[0] = start[0] + 1
        elif direction == 2:
            start[1] = start[1] + 1
        elif direction == 3:
            start[0] = start[0] - 1
        elif direction == 4:
            start[1] = start[1] - 1

        if i%10==0 :
            print('Now, here : {} by {}times'.format(start,i))

    print('Now, here : %s'%start)


if __name__ == '__main__':
    main()
