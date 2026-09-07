k = int(input("Enter number to count digits :"))
c = 0
while k > 0:
    c += 1
    k //= 10

print(c)