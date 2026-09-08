rf = int(input("Enter a four-digit number: "))
oa = rf % 10
ta = (rf // 10) % 10
ha = (rf // 100) % 10
fa = rf // 1000
print(oa * 1000 + ta * 100 + ha * 10 + fa)