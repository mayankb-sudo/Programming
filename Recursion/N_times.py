# Print Name N times using Recursion


'''
Problem Description: Given an integer N, write a program to print your name N times.

Examples
Input: N = 3
Output: Ashish Ashish Ashish 
Explanation: Name is printed 3 times.

Input: N = 1
Output: Ashish 
Explanation: Name is printed once.

'''


def n_times(name, N, c=0):
    if c == N:
        print(f"{N} is equal to Count")
        return
    print(f"Name : {name}")
    c+=1
    return n_times(name, N, c)


n_times("Mayank", 3)

'''
You use a counter c, which is fine, but usually recursion solutions avoid showing internal counters unless needed.

'''

# ####################################################################### #


def n_times(name, N):
    if N == 0:
        return
    print(name, end=" ")
    n_times(name, N - 1)

n_times("Mayank", 2)
