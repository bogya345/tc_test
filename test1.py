from msilib.schema import ControlEvent
import numpy as np
from time import sleep

def func1(x)->np.array:
    return x * 10 + 10

def func2(x:np.array, y:np.array)->np.array:
    
    for i in range(0,5):
        print('Gonna sleep')
        sleep(1)
        print(i)
        print('Gonna wake')
        continue

    return x.sum() + y.sum()

if __name__ == '__main__':
    
    x = np.arange(start=0, stop=100)
    print(x)

    y = func1(x)
    print(y)

    res = func2(x, y)
    print(x, y, res)
    pass