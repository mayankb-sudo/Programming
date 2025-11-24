# Check if a number is Armstrong Number or not


'''
Problem Statement:Given an integer N, return true it is an Armstrong number otherwise return false.

An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.


Example 1:
Input:N = 153
Output:True
Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153
                                        
Example 2:
Input:N = 371                
Output: True
Explanation: 3^3+7^3+1^3 = 27 + 343 + 1 = 371


'''
import math


num = int(input("Enter a Number: "))

digits = math.floor(math.log10(abs(num))) + 1
arm_num =0

print(arm_num,"arm_num")

for n in str(num) :
    arm_num += int(n)**digits

if arm_num == num:
    print(f"{arm_num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")




# 1634, 371, 8208, 9474, 407