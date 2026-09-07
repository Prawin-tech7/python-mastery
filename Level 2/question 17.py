def prime_checking(p_s):
    
    if p_s <= 1:
        return False
    
    for b in range(2,p_s):
        if p_s % b == 0:
            return False
    return True

p_s = input("Enter a number to check prime: ")
if not p_s.isdigit():
        print("Invalid input. Please enter a valid number.")

sum_p_s = 0
for j in range(len(p_s)):
    sum_p_s += int(p_s[j])


if prime_checking(int(p_s)) and sum_p_s == 14 :
    print("Prime & sum of digits is 14")
elif prime_checking(int(p_s)) and sum_p_s != 14:
    print("Prime but not sum of digits is 14 ")
elif not prime_checking(int(p_s)) and sum_p_s == 14:
    print("Not prime but sum of digits is 14")
else:
    print("Not Prime and sum of digits is not 14")
