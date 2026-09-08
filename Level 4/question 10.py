st = int(input("Enter a three-digit number: "))
print(st % 10 + (st // 10) % 10 + st // 100)