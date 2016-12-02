'''
PERFECT_SQUARE(number)
	total ← 1
	counter ← 1
	WHILE number ← total
		total ← counter * counter
		counter ← counter + 1
	IF total > number
		counter ← counter - 2
		total ← counter * counter
	RETURN total
'''

'''
Calculate highest square number, if n is not square, then round
down square root of input to nearest whole, then square it.

'''

import math

def perfect(n):
    sqrt = math.sqrt(n)                                     # 1
    
    if int(sqrt)*int(sqrt) == n:                            # n
        print(int(n))                                       # n
        # if the square root of the input squared is square
        # then input is highest perfect square
    else:                                                   # n
        square = (int(sqrt)**2)                             # n
        print(square)                                       # n
        # if not, then we take nearest whole number
        # and square it for answer

perfect(624)
        
