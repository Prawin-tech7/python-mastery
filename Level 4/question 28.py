def prime_checking(u):

    if u <= 1:
        return False

    for i in range(2,u):
        if u % i == 0:
            return False
    return True


for fp in range(1000,10000):
    if prime_checking(fp):
        print(fp)
        break