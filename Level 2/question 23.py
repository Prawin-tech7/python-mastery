import math

num_sqrt = input("Enter numbers for single digit perfect sq count : ")
c = 0
for l in range(len(num_sqrt)):
    if math.sqrt(int(num_sqrt[l])).is_integer() :
        c += 1
print(c)