def check_ascending(h):
    for m in range(len(h) - 1):
        if h[m] >= h[m + 1]:
            return False
    return True

h = input("Enter a number to check ascending or not :")

if check_ascending(h):
    print("Numbers are in ascending order")
else:
    print("Numbers are not in ascending order")
    