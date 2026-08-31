def biggest_digit_sum(c, d):
    if c > d:
        x = c
    else:
        x = d
    return (x // 10) + (x % 10)

if __name__ == "__main__":
    c = int(input("Enter first number: "))
    d = int(input("Enter second number: "))
    print(biggest_digit_sum(c, d))
