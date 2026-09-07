def check_same(u,v):
    if u == v :
        return "Same"
    else:
        return "Not Same"

u = int(input("Enter first number: "))
v = int(input("Enter second number: "))

g = check_same(u,v)
print(g)