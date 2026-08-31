def make_ones_two(t):
    return (t // 10) * 10 + 2

if __name__ == "__main__":
    t = int(input("Enter number: "))
    print(make_ones_two(t))
