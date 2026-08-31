def odd_subtract(v):
    return v - 5 * (v % 2)

if __name__ == "__main__":
    v = int(input("Enter number: "))
    print(odd_subtract(v))
