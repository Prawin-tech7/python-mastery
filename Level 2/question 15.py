o = input("Enter numbers for to subract 1 from 1st digit if odd :")

if int(o[0]) % 2 == 0:
    print(o)
else:
    print(str(int(o[0]) - 1) + o[1:])