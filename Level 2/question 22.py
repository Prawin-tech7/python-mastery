a = int(input("Enter a number to count two-digit odd numbers: "))
c = 0

for i in range(len(str(a)) - 1):
    two_digit_num = int(str(a)[i:i+2])
    
    if two_digit_num % 2 == 1:
        c += 1

print(c)