#  Pattern-1: Rectangular Star Pattern


'''
Problem Statement: Given an integer N, print the following pattern.

Example 1:
Input: N = 3
Output: 
* * *
* * *
* * *


Example 2:
Input: N = 6
Output:
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *

'''

N = int(input("Enter the value of N : "))
print(f"The Value of N is {N}")

for i in range(N):   # iter N times 
    print("* " * N)   # for each iteration it prints N times 



#---------------------- TIME COMPLEXITY  O(N^2) -------------------#

'''
Time complexity is N * N as first loop do the work N times and print also work for N times in each iteration

'''
