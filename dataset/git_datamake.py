import numpy as np
import sys


def main():
    print('Which do you choice data name (occupancy or gausu)?\n')
    data_name = input('data name:  ')

    if data_name == 'occupancy':
        sys.path.append('implementation/Occupancy_data')
        from Occupancy_def import Occupancy_set
        Occupancy_set()

    elif data_name == 'gausu':
        sys.path.append('implementation/Sampletest')
        data_type = input('liner or not liner or circle?  :')
        if data_type == 'liner':
            from gauss_sample import two_class
            two_class()

        elif data_type == 'not liner':
            from gauss_sample import no_liner
            no_liner()
        elif data_type == 'circle':
            from gauss_sample import circle
            circle()
        else:
            print('no data')

    else:
        print('Not exist this data')

if __name__ == '__main__':
    main()
