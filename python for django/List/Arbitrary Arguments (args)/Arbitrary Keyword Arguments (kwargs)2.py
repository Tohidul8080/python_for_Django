#arbitrary keyword arguments

def fun2(**kwargs):
    print(kwargs)

#fun2(name="tohidul", lname="islam", age=25)

def hello3(*args, **kwargs):
    print(args, kwargs)

#hello3("tohidul",name="tohiudl islam",age=23)
#hello3(name="tohiudl islam",age=23)