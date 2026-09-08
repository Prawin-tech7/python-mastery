def prime_checking(a):
    if a <= 1:
        return False
    for b in range(2, int(a ** 0.5) + 1):
        if a % b == 0:
            return False
    return True

pc = 0

for c in range(2, 1000000):
    if prime_checking(c):
        ds = 0
        for d in str(c):
            ds += int(d)
        if ds == 14:
            pc += 1

print(pc)
