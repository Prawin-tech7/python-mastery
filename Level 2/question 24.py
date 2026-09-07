import math 

n_sqrt = int(input("Enter a number to count two-digit perfect square :  "))
c = 0

for v in range(len(str(n_sqrt)) - 1):
    two_digit_num = int(str(n_sqrt)[v:v+2])
    
    if math.sqrt(two_digit_num).is_integer() :
        c += 1

print(c)
