def prime_check(m):
    
    if m <= 1:
        return False
    
    for n in range(2, m):
        if m % n == 0:
            return False
    return True

g = input("Enter numbers to count total number of prime numbers :")
h = 0

for y in range(len(g)):
    if prime_check(int(g[y])):
        h += 1

print(h)
