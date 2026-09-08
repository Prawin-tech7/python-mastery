def prime_checking(v):

    if v <= 1:
        return False

    for f in range(2,v):
        if v % f == 0:
            return False
    return True


for fp in range(9999,999,-1):
    if prime_checking(fp):
        print(fp)
        break