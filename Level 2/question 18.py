def prime_checking(q_b):
    
    if q_b <= 1:
        return False
    
    for c in range(2, q_b):
        if q_b % c == 0:
            return False
    return True


q_b = int(input("Enter a number to check whether its last two digits are prime: "))
q_last = q_b % 100

if prime_checking(q_last):
    print("Prime")
else:
    print("Not Prime")