def reverse_three(hk): 
    a = hk // 100 
    b = (hk // 10) % 10 
    c = hk % 10 
    return c * 100 + b * 10 + a 

if __name__ == "__main__": 
    hk = int(input("Enter number: ")) 
    print(reverse_three(hk))