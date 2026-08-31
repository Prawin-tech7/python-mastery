def reverse_three(o): 
    a = o // 100 
    b = (o // 10) % 10 
    c = o % 10 
    return c * 100 + b * 10 + a 

if __name__ == "__main__": 
    o = int(input("Enter number: ")) 
    print(reverse_three(o))