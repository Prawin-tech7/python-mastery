def prime_checking(r):

    if r <= 1:
        return False

    for c in range(2,r):
        if r % c == 0:
            return False
    return True


hc = 0

for h in range(100,1000):
    if prime_checking(h):
        hc += 1

print(hc)