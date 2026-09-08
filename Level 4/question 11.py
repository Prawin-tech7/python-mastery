sf = int(input("Enter a four-digit number: "))
print(sf % 10 + (sf // 10) % 10 + (sf // 100) % 10 + sf // 1000)