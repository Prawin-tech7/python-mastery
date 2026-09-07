c = input("Enter a number to count odd digits: ")

odd_count = 0
for k in range(len(c)):
    if int(c[k]) % 2 != 0:
        odd_count += 1

print(odd_count)