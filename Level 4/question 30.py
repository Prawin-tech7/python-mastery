def prime_checking(g):

    if g <= 1:
        return False

    for a in range(2,g):
        if g % a == 0:
            return False
    return True


for ep in range(99999999,9999999,-1):
    if prime_checking(ep):
        print(ep)
        break