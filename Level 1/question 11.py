def sum_two_digits(k): 
    return (k // 10) + (k % 10) 

if __name__ == "__main__": 
    k = int(input("Enter number: ")) 
    print(sum_two_digits(k))