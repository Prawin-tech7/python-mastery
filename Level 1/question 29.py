def check_middle_sum(d):
    h = (d // 100) % 10
    t = (d // 10) % 10

    if h + t > 10:
        return "Success"
    return "Failure"

if __name__ == "__main__":
    d = int(input("Enter number: "))
    print(check_middle_sum(d))
