def reverse_last_two(p):
    a = p // 100
    b = (p // 10) % 10
    c = p % 10

    return a * 1000 + c * 100 + b * 10

if __name__ == "__main__":
    p = int(input("Enter number: "))
    print(reverse_last_two(p))