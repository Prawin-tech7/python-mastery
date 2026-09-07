def prime_checking(p):
    
    if p <= 1:
        return False
    
    for b in range(2,p):
        if p % b == 0:
            return False
    return True


p = int(input("Enter a number to check prime: "))

if prime_checking(p):
    print("Prime")
else:
    print("Not Prime")
