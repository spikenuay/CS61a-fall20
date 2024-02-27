
from operator import floordiv,mod

def divide_exact(n,d):
    return floordiv(n,d),mod(n,d) 

q,r = divide_exact(2013,10)

def abs_value(x):
    if x< 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x

