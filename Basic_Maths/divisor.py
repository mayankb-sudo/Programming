# Print all Divisors of a given Number


'''

Problem Statement: Given an integer N, return all divisors of N.
A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

Examples
Input: N = 36
Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]  
Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.

Input: N = 12
Output: [1, 2, 3, 4, 6, 12]
Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.

'''
N=36

divisor=[]
for i in range(1, N + 1):
    if N % i == 0:
        divisor.append(i)

print(divisor,"divisor")





# ------------------------OPTIMAL APPROACH-----------------------------------

N = int(input("Enter N: "))

divisors = []

i = 1
while i <= N**0.5:
    if N % i == 0:
        divisors.append(i)

        # Add the pair divisor if it's different
        if i != N // i:
            divisors.append(N // i)
    i += 1

divisors.sort()

print(divisors, "divisors")
