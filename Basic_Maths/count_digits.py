# Count all Digits of a Number

'''
You are given an integer n. You need to return the number of digits in the number.



The number will have no leading zeroes, except when the number is 0 itself.


Examples:
Input: n = 4

Output: 1

Explanation: There is only 1 digit in 4.

Input: n = 14

Output: 2

Explanation: There are 2 digits in 14.

'''

N = 123

count = 0

while N>0:
    count+=1
    N= N//10
print(count)


n= 234
digits = len(str(n))
print(digits, "digits")


#    ------------------BEST Time Complexity o(1) --------------------------
import math

n = 1235
digits = math.floor(math.log10(abs(n))) + 1

print(digits, "123")


