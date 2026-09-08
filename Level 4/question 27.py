def prime_checking(w):

    if w <= 1:
        return False

    for y in range(2,w):
        if w % y == 0:
            return False
    return True


for lp in range(999,99,-1):
    if prime_checking(lp):
        print(lp)
        break