
def check_sum_ten(a):
    x = a // 10
    y = a % 10

    if x + y == 10:
        return "Success"
    return "Failure"

if __name__ == "__main__":
    a = int(input("Enter number: "))
    print(check_sum_ten(a))
