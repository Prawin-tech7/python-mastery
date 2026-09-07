n = input("Enter number for interchanging first and last digit : ")
print(int(n[-1] + n[1:-1] + n[0]))