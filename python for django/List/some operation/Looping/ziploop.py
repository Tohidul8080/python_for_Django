#zip
myList=["A","B","C","D","E"]
myList1=[2,7,5,3,9,8]
for i, j in zip(myList, myList1):
    print(i,j)

for z in reversed( sorted(myList1)):
    print(z)