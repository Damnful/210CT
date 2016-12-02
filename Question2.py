'''
This function uses the prime factor method of calculating trailing
zeroes instead of calculating the factorial. This means that we count
the number of times our target number is divisible by 5. This also includes
powers of five
'''
def factorial_zeroes(n):
 
    power = 0						         # (1)
    zeroes = 0							 # (1)
 
    while n >= (5**power):					 # (n)
        power += 1						 # (n)
    #this while loop is used to include any powers of five if needed

    for i in range(1,power):					 # (n)
        zeroes = zeroes + (n // (5**i))				 # (n)
    #this divides the factorial by each power of five and sums the total
 
    print(str(n) + "! has " + str(zeroes) + " trailing zeroes")  # (1)
 
factorial_zeroes(250) 
