# Sum of First N Numbers

'''
Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.


Examples:


Input : N = 4
Output : 10
Sum is 1 + 2 + 3 + 4 => 10.

Input : N = 2
Output : 3
Sum is 1 + 2 => 3.

'''



def sum(n):
    if n==0:
        return 0
    return n + sum(n-1)
    
print(sum(4))