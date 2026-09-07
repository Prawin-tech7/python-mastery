def prime_checking(m):
    
    if m <= 1:
        return False
    
    for n in range(2, m):
        if m % n == 0:
            return False
    return True


h = 0
for p in range(1, 10):
    if prime_checking(p):
        h += 1

print(h)