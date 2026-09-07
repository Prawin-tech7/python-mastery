def count_numbers_sum():
    count = 0
    for i in range(100000):
    
        digit_sum = sum(int(digit) for digit in str(i))
        if digit_sum == 14:
            count += 1
            
    print(f"Total count of numbers: {count}")
count_numbers_sum()
