def odd_sum_subtract(x):
    a = x // 10
    b = x % 10
    s = a + b

    return x - 5 * (s % 2)

if __name__ == "__main__":
    x = int(input("Enter number: "))
    print(odd_sum_subtract(x))
