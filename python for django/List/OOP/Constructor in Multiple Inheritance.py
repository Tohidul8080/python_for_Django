class A:
    def __init__(self, name):
        self.name=name

    def hello(self):
        print("Hello from Class A")


class B:
    def __init__(self, job):
        self.job=job

class C(A,B):
    def __init__(self, name, job):
        A.__init__(self, name)
        B.__init__(self, job)


    def hello(self):
        print(f"{self.name} is {self.job}")

obj=C("tohidul", "islam")

obj.hello()
        