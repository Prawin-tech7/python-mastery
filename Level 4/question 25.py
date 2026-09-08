def prime_checking(q):

    if q <= 1:
        return False

    for t in range(2,q):
        if q % t == 0:
            return False
    return True


hp = 0

for pr in range(100,1000):
    if prime_checking(pr):
        hp += pr

print(hp)