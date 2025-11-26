# Check if a number is prime or not

N = int(input("Enter a number: "))
if N <= 1:
    print("Enter Positive Value")
else:
    for i in range(2, N):  
        if N % i == 0:
            print(f"{N} is not Prime Number")
            break
        else:
            print(f"{N} is not Prime Number")



# -------------------------OPTIMAL APPROACH ---------------------------

N = int(input("Enter a number: "))

if N <= 1:
    print("Enter positive value greater than 1")
else:
    is_prime = True
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{N} is a Prime Number")
    else:
        print(f"{N} is not a Prime Number")
