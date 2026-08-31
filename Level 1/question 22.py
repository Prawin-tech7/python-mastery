def odd_tens_subtract(w):
    t = (w // 10) % 10

    return w - 5 * (t % 2)

if __name__ == "__main__":
    w = int(input("Enter number: "))
    print(odd_tens_subtract(w))