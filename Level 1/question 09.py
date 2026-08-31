def get_hundred(i): 
    return (i // 100) % 10 

if __name__ == "__main__": 
    i = int(input("Enter number: ")) 
    print(get_hundred(i))