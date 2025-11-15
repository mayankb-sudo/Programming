# Pattern - 8: Inverted Star Pyramid


'''
Problem Statement: Given an integer N, print the following pattern : 


Here, N = 5.

Examples:

Input Format: N = 3
Result: 
*****  
 ***
  *   
Input Format: N = 6
Result:     
***********
 *********
  *******
   ***** 
    ***    
     *

'''


# N = int(input("Enter the value of N : "))
N = 4
print(f"The Value of N is {N}")
for row in range(N, 0, -1):
    spaces = ((N-row)*" ")
    stars = (((2*row)-1) * "*")
    print(spaces + stars)