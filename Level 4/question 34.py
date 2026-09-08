pc = 0

for f in range(1,100000):
    if str(f) == str(f)[::-1]:
        pc += 1

print(pc)