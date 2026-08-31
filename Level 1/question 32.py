def single_digit(f):
    while f >= 10:
        s = 0
        while f > 0:
            s += f % 10
            f //= 10
        f = s
    return f

if __name__ == "__main__":
    f = int(input("Enter number: "))
    print(single_digit(f))