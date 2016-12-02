def is_prime(n, x=2):
    if n <= 1:
        print(str(n) + " is not a prime number")
    elif x == n:
        print(str(n) + " is a prime number")
        # if the counter reaches the input, the input is prime
    else:
        if n % x != 0:
            is_prime(n, x+1)
        # this if statement is the root to the solution
        # x is a counter that the input is divided against
        else:
            print(str(n) + " is not a prime number")
        # if at any point there isn't a remainder, then input is not prime
 
is_prime(547)
