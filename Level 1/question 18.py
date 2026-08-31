def make_tens_one(s):
    return 10 + (s % 10)

if __name__ == "__main__":
    s = int(input("Enter number: "))
    print(make_tens_one(s))
