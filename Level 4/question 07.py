rt = int(input("Enter a three-digit number: "))
oa = rt % 10
ta = (rt // 10) % 10
ha = rt // 100
print(oa * 100 + ta * 10 + ha)