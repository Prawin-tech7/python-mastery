def check_ends_sum(c):
    x = c // 100
    y = c % 10

    if x + y < 10:
        return "Success"
    return "Failure"

if __name__ == "__main__":
    c = int(input("Enter number: "))
    print(check_ends_sum(c))

