# Pattern - 3: Right-Angled Number Pyramid

'''
Problem Statement: Given an integer N, print the following pattern : 

Examples:

Input Format: N = 3
Result: 
1
1 2 
1 2 3

Input Format: N = 6
Result:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6

'''


N = int(input("Enter the value of N : "))
print(f"The Value of N is {N}")

for row in range(1,N+1):
    for col in range(1, row+1):
        print(col, end=" ")
    print()






#---------------------- TIME COMPLEXITY  O(N^2) -------------------#

'''

Outer loop (for row in range(1, N + 1):)

Runs N times (from 1 to N).

Inner loop (for col in range(1, row + 1):)

For each row, the inner loop runs row times.

So the number of total inner loop executions = 1 + 2 + 3 + ... + N

That's the sum of the first N natural numbers:

 N(N + 1) / 2,


Therefore, total time complexity = O(N²).

Each print(col, end=" ") operation is O(1), so it doesn't change the overall order.

'''

