def same_middle_subtract(z):
    h = (z // 100) % 10
    t = (z // 10) % 10

    return z - 5 * (h == t)

if __name__ == "__main__":
    z = int(input("Enter number: "))
    print(same_middle_subtract(z))