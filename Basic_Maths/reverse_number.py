#  Reverse Digits of A Number

'''

Problem Statement: Given an integer N return the reverse of the given number.

Note: If a number has trailing zeros, then its reverse will not include them. 
For e.g., reverse of 10400 will be 401 instead of 00401.

'''



N = int(input("Enter a number: "))

reverse_num = 0
num = N

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10

print("Reversed number:", reverse_num)
