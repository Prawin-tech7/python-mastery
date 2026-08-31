def check_three_sum(b):
    x = b // 100
    y = (b // 10) % 10
    z = b % 10

    if x + y + z == 10:
        return "Success"
    return "Failure"

if __name__ == "__main__":
    b = int(input("Enter number: "))
    print(check_three_sum(b))
