# Object Oriented Projramming
# Inheritance

class A:
    def __init__(self, name):
        self.name=name

    def hello(self):
        print(f"{self.name}")

class B(A):
    pass


obj= B("tohidul")
obj.hello()