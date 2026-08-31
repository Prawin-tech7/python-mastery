def middle_digit(j): 
    return (j // 10) % 10 

if __name__ == "__main__": 
    j = int(input("Enter number: ")) 
    print(middle_digit(j))