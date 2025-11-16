# Pattern - 9: Diamond Star Pattern


'''
Problem Statement: Given an integer N, print the following pattern : 



Examples:

Input Format: N = 3
Result: 
  *  
 ***
***** 
*****  
 ***
  *   
Input Format: N = 6
Result:   
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *

'''


# N = int(input("Enter the value of N : "))
N = 3
print(f"The Value of N is {N}")
for row in range(1,N+1):
    print(((N-row)*" ") + (((2*row)-1) * "*"))
for row in range(N, 0, -1):
    print(((N-row)*" ") + (((2*row)-1) * "*"))