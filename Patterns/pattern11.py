# Pattern - 11: Binary Number Triangle Pattern


'''
Problem Statement: Given an integer N, print the following pattern : 



Examples:

Input Format: N = 3
Result: 
1
01
101

Input Format: N = 6
Result:   
1
01
101
0101
10101
010101

'''


# N = int(input("Enter N: "))
N = 5

for row in range(1, N+1):
    pattern = ""
    
    # starting digit (1 for odd row, 0 for even row)
    start = 1 if row % 2 != 0 else 0
    
    for col in range(row):
        pattern += str((start + col) % 2)
    
    print(pattern)
