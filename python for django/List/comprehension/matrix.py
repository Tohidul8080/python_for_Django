myList=[letter.upper() for letter in "bangladesh"]
myl=[l.lower() for l in "THIS IS TOHIDUL ISLAM"]
print(myl)
print(myList)

#Nested loop
# 0 1 2 3
# 0 1 2 3
# 0 1 2 3
# matrix=[0,1,2,3],[0,1,2,3],[0,1,2,3]

matrix=[]
for i in range(3):
    matrix.append([])
    for j in range(4):
        matrix[i].append(j)


myMatrix=[[j for j in range(4) for i in range(3)]]
print(myMatrix)

flatList=[i[0] for i in myMatrix]
print("flat=",flatList)

print(matrix)