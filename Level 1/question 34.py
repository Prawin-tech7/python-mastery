def bigger_tens_difference(e, f):
    te = (e // 10) % 10
    tf = (f // 10) % 10

    if te > tf:
        x = e
    else:
        x = f

    one = x % 10
    hundred = x // 100

    return abs(one - hundred)

if __name__ == "__main__":
    e = int(input("Enter first number: "))
    f = int(input("Enter second number: "))

    print(bigger_tens_difference(e, f))
