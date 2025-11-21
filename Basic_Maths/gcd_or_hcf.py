'''
You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.



The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.


Examples:
Input: n1 = 4, n2 = 6

Output: 2

Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6

Greatest Common divisor = 2.



Input: n1 = 9, n2 = 8

Output: 1

Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.

Greatest Common divisor = 1.

'''


#------------------------------BRUTE FORCE------------------------------
N=6
div=set()
for i in range(1, N+1):
    if N % i == 0 :
        div.add(i)

M=4
div1=set()
for i in range(1, M+1):
    if M % i == 0 :
        div1.add(i)

hcf_list = list(div & div1)
print(hcf_list, "HCF LIST")
print(hcf_list[-1], 'hcf')

# ----------------------------------------------------------------------------------------------------------------------

# --------------------------------------Better Approach-----------------------------------------------------------------

gcd = 1
n1=6
n2=4
for i in range(1, min(n1, n2) + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
print(gcd, "gcd")

#----------------------------------------------------------------------------------------------------------------------

# -----------------------------------------Best--------------------------------------------------------------------------
a = 15
b = 20

while a > 0 and b > 0:
    if a > b:
        a = a % b
        print(a, "A")
    else:
        b = b % a
        print(b, "B")

if a == 0:
    print("GCD =", b)
else:
    print("GCD =", a)


