# reduce 
from functools import reduce
li=[1,2,3,4,5,4,7]

def func(x, y):
    return x+y
#sum=reduce(func, li)
sum=reduce(lambda x, y: x+y, li)
print(sum)