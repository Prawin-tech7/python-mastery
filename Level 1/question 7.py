def get_tens(g): 
    return (g // 10) % 10 

if __name__ == "__main__": 
    g = int(input("Enter number: ")) 
    print(get_tens(g))