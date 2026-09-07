def sum_14(c):
    tot = 0
    for q in range(len(c)):
        tot += int(c[q])

    if tot == 14:
        return True
    return False

c = input("Enter a number to check whether its sum of digits is 14 :")
print(sum_14(c))
