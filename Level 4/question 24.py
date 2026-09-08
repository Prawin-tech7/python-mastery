def prime_checking(s):

    if s <= 1:
        return False

    for z in range(2,s):
        if s % z == 0:
            return False
    return True


sp = 0

for tp in range(10,100):
    if prime_checking(tp):
        sp += tp

print(sp)