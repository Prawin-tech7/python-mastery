def same_ends_subtract(y):
    a = y // 100
    b = y % 10

    return y - 5 * (a == b)

if __name__ == "__main__":
    y = int(input("Enter number: "))
    print(same_ends_subtract(y))