n = int(input("Enter the size of the pattern (n): "))

for i in range(n):
    left_part = [chr(97 + (n - j - 1)) for j in range(i + 1)] 
    right_part = left_part[:-1][::-1]  
    row = left_part + right_part 
    print('-'.join(row).center((n * 2 - 1) * 2 - 1, '-')) 

for i in range(n - 2, -1, -1): 
    left_part = [chr(97 + (n - j - 1)) for j in range(i + 1)]  
    right_part = left_part[:-1][::-1]  
    row = left_part + right_part  
    print('-'.join(row).center((n * 2 - 1) * 2 - 1, '-'))