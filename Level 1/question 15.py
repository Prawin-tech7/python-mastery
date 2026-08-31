def reverse_first_two(q):
    a = q // 1000
    b = (q // 100) % 10
    c = (q // 10) % 10
    d = q % 10

    return b * 1000 + a * 100 + c * 10 + d

if __name__ == "__main__":
    q = int(input("Enter number: "))
    print(reverse_first_two(q))