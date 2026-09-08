ca = [6,12,3,15,7]

for j in range(len(ca)-1,0,-1):
    if ca[j] >= 10:
        ca[j-1] += ca[j] // 10
        ca[j] %= 10

print(*ca)