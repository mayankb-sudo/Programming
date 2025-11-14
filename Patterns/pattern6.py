# Pattern - 6: Inverted Numbered Right Pyramid

'''

Problem Statement: Given an integer N, print the following pattern : 



Examples:

Input Format: N = 3
Result: 
1 2 3
1 2
1

Input Format: N = 6
Result:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1

'''



N = int(input("Enter the value of N : "))
print(f"The Value of N is {N}")
for row in range(1,N+1):
    for column in range(1, (N+2)-row):
        print(column, end = " ")
    print()


'''
for row in range(N, 0, -1):
    # Loop for numbers in each row
    for col in range(1, row + 1):
        print(col, end=" ")
    print()
'''