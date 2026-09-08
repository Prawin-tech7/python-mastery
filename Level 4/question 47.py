def add_large_arrays(a, b):
    n1 = int("".join(map(str, a)))
    n2 = int("".join(map(str, b)))
    total = n1 + n2
    return list(map(int, str(total)))

list1 = list(map(int, input("Enter first array in comma separated values: ").split(",")))
list2 = list(map(int, input("Enter second array in comma separated values: ").split(",")))
ans = add_large_arrays(list1, list2)
print(ans)
