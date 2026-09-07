l = int(input("Write numbers to sum :"))
s = 0
while l > 0:
    s += l % 10
    l //= 10

print(s)