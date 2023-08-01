# higher order Function

def hof(fn):
    print(fn.__name__)
    fn()

def greet():
    print("hello world!")

def hello():
    print("hello bohubrihi")

hof(greet)

li=[1,2,3,4,5,6,7]

newList=list(filter(lambda x: x%2==1, li))
print(newList)

l2=[3,5,7,8,9,10]
def myFilter(fu, l):
    newL=[]
    for i in l:
        if fu(i):
              newL.append(i)
    return newL


ne=myFilter(lambda x: x%2==1, l2)