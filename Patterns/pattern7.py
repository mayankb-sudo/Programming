# Pattern - 7: Star Pyramid

'''
Problem Statement: Given an integer N, print the following pattern : 


Examples:

Input Format: N = 3
Result: 
  *  
 *** 
*****   

Input Format: N = 6
Result:
     *     
    ***    
   *****   
  *******  
 ********* 
***********

'''


N = int(input("Enter the value of N : "))
print(f"The Value of N is {N}")
for row in range(1,N+1):
    spaces = ((N - row)*" ")
    stars = (((2*row)-1) * "*")
    print(spaces + stars)

