# Function
def hello(fname, lname):
    print(f"{fname} {lname}")

# fname, lname -> parameter
# arguments -> tohidul , islam (Passed Value)
# hello ("tohidul", "islam")

hello("tohidul", "islam")


def fun1(*args):
    print(args)

fun1("tohidul","islam", 25, True, False)