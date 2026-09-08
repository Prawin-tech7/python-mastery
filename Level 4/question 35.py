lm = int(input("Enter first number: "))
ln = int(input("Enter second number: "))

mx = max(lm,ln)
while True:
    if mx % lm == 0 and mx % ln == 0:
        print(mx)
        break
    mx += 1