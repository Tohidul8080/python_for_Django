# filter function
l=[2,4,5,6,7,8,10]

def func(n):
    return n%2==1

#newist=list(filter(lambda n: n%2==1, l))
newist=list(filter(func, l))
print(newist)