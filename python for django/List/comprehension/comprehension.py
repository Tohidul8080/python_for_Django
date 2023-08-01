#comprehension
myList=[1,3,4,8,9,2]
newList=[]
for i in myList:
    if i%2==1:
     newList.append(i*i)

#comList=[i+2 for i in myList]
comList=[i*i for i in myList if i%2==1]

print("Old list:",myList)
print("New list:",newList)
print("com list",comList)