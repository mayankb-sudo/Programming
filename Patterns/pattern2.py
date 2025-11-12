#  Pattern-2: Right-Angled Triangle Pattern

'''
Problem Statement: Given an integer N, print the following pattern : 

Here, N = 5.

Examples:

Input Format: N = 3
Result: 
* 
* * 
* * *

Input Format: N = 6
Result:
* 
* * 
* * *
* * * *
* * * * *
* * * * * *

'''


N = int(input("Enter the value of N : "))
print(f"The Value of N is {N}")

for i in range(1,N+1):   
    print("* " * i)






#---------------------- TIME COMPLEXITY  O(N^2) -------------------#

'''

The loop runs from i = 1 to i = N, so there are N iterations in total.
For each iteration:

"*" * i creates a string of i stars → this operation takes O(i) time.

print() prints that string → also O(i) time.

Therefore, the total time for each iteration is O(i).

To get the total time, we sum the work done in all iterations:

Total time = O(1 + 2 + 3 + ... + N)

The sum of the first N natural numbers is N(N + 1) / 2,
so the total time complexity becomes:

O(N²)


'''

