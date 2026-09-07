def prime_checking(d):
    
    if d <= 1:
        return False
    
    for b in range(2, d):
        if d % b == 0:
            return False
    return True


d = int(input("Enter a number to check prime: "))

if prime_checking(d):
    print("Number is Prime")
else:
    print("Number is not Prime")