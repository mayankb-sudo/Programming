# Print N to 1 using Recursion

'''
Problem Description: Given an integer N, write a program to print numbers from N to 1.

Examples
Input: N = 4
Output: 4, 3, 2, 1
Explanation: All the numbers from 4 to 1 are printed.

Input: N = 1
Output: 1 
Explanation: This is the base case.

'''

def till_n(n):
    if n==0:
        return
    print(n, end=" ")
    
    return till_n(n-1)
    
till_n(4)