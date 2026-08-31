def zero_tens(u):
    return (u // 100) * 100 + (u % 10)

if __name__ == "__main__":
    u = int(input("Enter number: "))
    print(zero_tens(u))
