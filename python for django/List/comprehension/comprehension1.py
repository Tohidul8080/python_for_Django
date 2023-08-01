#comprehension
#iterable -> List, Tuple, Dictionary
#create -> List, Dictionary, Set

myist=[1,2,3,4,7,9]

newist=list([i+1 for i in myist])
print(newist)
newTuple=tuple(i+2 for i in myist)
newSet={i*2 for i in myist}
newTList=[(i, i*2, i**3) for i in myist]
print("L=",newTList)
print(newSet)
print(newTuple)

#from dictionary
myDict={"name":"tohidul","age":25,"country":"bangladesh","bti":3}
Nset={i for i in myDict.items()}
Nlist=[(key,value) for key, value in myDict.items()]
NDict={key+"key": value for key, value in myDict.items()}
print("N=",NDict)
print(Nlist)

print(Nset)


