def bigger_outer_sum(g, h):
    g_sum = (g // 100) + (g % 10)
    h_sum = (h // 100) + (h % 10)
    if g_sum > h_sum:
        x = g
    else:
        x = h
    return (x // 100) + ((x // 10) % 10) + (x % 10)

if __name__ == "__main__":
    g = int(input("Enter first number: "))
    h = int(input("Enter second number: "))
    print(bigger_outer_sum(g, h))