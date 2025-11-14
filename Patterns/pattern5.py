# Pattern-5: Inverted Right Pyramid

'''

Problem Statement: Given an integer N, print the following pattern : 


Here, N = 5.

Examples:

Input Format: N = 3
Result: 
* * *
* * 
*

Input Format: N = 6
Result:
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 

'''


N = int(input("Enter the value of N : "))
print(f"The Value of N is {N}")
for row in range(1,N+1):
    print("*" * ((N-row)+1) )






#---------------------- TIME COMPLEXITY  O(N^2) -------------------#

'''
The outer loop for row in range(1, N + 1) runs N times (from 1 to N).

Inside the loop, we have "*" * ((N - row) + 1) which creates a string of stars.

When row = 1, number of stars = N

When row = 2, number of stars = N - 1

When row = 3, number of stars = N - 2

...

When row = N, number of stars = 1

So, the number of stars printed in total =
N + (N - 1) + (N - 2) + ... + 1

This is the sum of the first N natural numbers in reverse order, which equals:

 N(N + 1) / 2,
	​


Each "*" * k operation and print() call takes O(k) time (because it creates and prints k characters).

Total Time Calculation

Total time = O(N + (N - 1) + (N - 2) + ... + 1)
= O(N(N + 1) / 2)
= O(N²)

Hence, the overall time complexity is O(N²).




'''

