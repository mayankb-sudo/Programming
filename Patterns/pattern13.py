# Pattern - 13: Increasing Number Triangle Pattern


'''
Problem Statement: Given an integer N, print the following pattern :

Examples
Input Format: N = 3
Result: 

1 
2 3 
4 5 6


Input Format: N = 6
Result:   

1 
2 3 
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21



'''


N = 8

number = 1
for row in range(1, N + 1):
    for column in range(1, row + 1):
        print(number, end=" ") 
        number += 1  
    print() 