a = int(input("Enter a 4-digit number to check its middle two digits: "))

b = (a // 10) % 100
c = 0

for d in range(1, b + 1):
    if b % d == 0:
        c += 1

if c == 2:
    print("Prime")
else:
    print("Not Prime")