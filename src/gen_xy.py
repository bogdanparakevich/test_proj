import numpy as np

def get_array(shape, dtype):
    return np.zeros(shape, dtype=dtype)


if __name__ == '__main__':
    array = get_array((3,3), 'float64')
    print(array)