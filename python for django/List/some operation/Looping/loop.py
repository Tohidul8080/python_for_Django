#Looping through Sequences
#looping
# for i in tuple, list, dictionary, set

myTuple=("A","B","C","D","E")
myList=[("a", 1), ("b", 2),("c",3)]
myList1=[("a", 1, "b"), ("b", 2,"r"),("c",3,'o')]

myDict={"name":"tohidul islam","age":25,"country":"bangladesh"}
mySet={"b","t","d","p"}
myStr="bangladesh"
for l in myStr:
    print(l)

for d in mySet:
    print(d)
#for t,p in myDict.items():
for key, value in myDict.items():
    #print(f"{t}  {p}")
    print(f"{key} {value}")

for i ,y,z in myList1:
    print(f"{i} {y} {z}")
