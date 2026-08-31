def check_middle_condition(e):
    h = (e // 100) % 10
    t = (e // 10) % 10

    if h + t == 10 and (h > 7 or t > 7):
        return "Success"
    return "Failure"

if __name__ == "__main__":
    e = int(input("Enter number: "))
    print(check_middle_condition(e))
