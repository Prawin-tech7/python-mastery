def prime_checking(p):

    if p <= 1:
        return False

    for b in range(2,p):
        if p % b == 0:
            return False
    return True


pc = 0

for tp in range(10,100):
    if prime_checking(tp):
        pc += 1

print(pc)