def prime_checking(n):

    if n <= 1:
        return False

    for m in range(2,n):
        if n % m == 0:
            return False
    return True


for sp in range(100,1000):
    if prime_checking(sp):
        print(sp)
        break