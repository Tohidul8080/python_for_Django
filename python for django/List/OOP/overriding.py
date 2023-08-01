# overriding

class A:
    def __init__(self, name):
        self.name=name

    def hello(self):
        print("Hello from Class A")

class B(A):
    def __init__(self):
        pass

    def hello(self):
        print("Hello from class B")


obj=B()
obj.hello()