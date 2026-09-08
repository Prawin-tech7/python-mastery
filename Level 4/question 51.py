ms = input("Enter a string: ")
fc = input("Enter a character: ")

for l in range(len(ms)):

    if ms[l] == fc:
        print(l + 1,end=" ")