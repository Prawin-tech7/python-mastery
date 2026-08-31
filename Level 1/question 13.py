def reverse_two(m): 
    return (m % 10) * 10 + (m // 10) 

if __name__ == "__main__": 
    m = int(input("Enter number: ")) 
    print(reverse_two(m))