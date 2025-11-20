'''
Problem Statement: Given an integer N, return true if it is a palindrome else return false.

A palindrome is a Nber that reads the same backward as forward. 
For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.


'''


N = int(input("Enter a Number: "))

RN = 0
num = N
while num > 0:
    digit = num % 10
    RN = RN * 10 + digit
    num //= 10

if N == RN:
    print(f"{N} is a palindrome number")
else:
    print(f"{N} is not a palindrome number")
