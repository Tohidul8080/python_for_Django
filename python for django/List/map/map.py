def func(n):
    return n+1

l=[3,6,4,2,8,9]

#newL=tuple(map(func,l))
newL=list(map(lambda n: n+1, l))
print(newL)



l=["tohidul islam","bohubrihi", "dhaka"]
l2=list(map(list,l))
print(l2)