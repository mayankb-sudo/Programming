# Print 1 to N using Recursion

'''
Problem Description: Given an integer N, write a program to print numbers from 1 to N.

Examples
Input: N = 4
Output: 1, 2, 3, 4
Explanation: All the numbers from 1 to 4 are printed.

Input: N = 1
Output: 1 
Explanation: This is the base case.

'''

def till_n(n, c=1):
    if n<c:
        return
    print(c)
    
    return till_n(n, c+1)
    
till_n(1)


# ====================================================================


def till_n(n):
    if n==0:
        return    
    till_n(n-1)
    print(n, end=" ")
    
till_n(5)