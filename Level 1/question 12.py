def sum_three_digits(l): 
    return (l // 100) + ((l // 10) % 10) + (l % 10) 

if __name__ == "__main__": 
    l = int(input("Enter number: ")) 
    print(sum_three_digits(l))