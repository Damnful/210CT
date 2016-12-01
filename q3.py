def perfect(n):
    square = 1
    counter = 1

    while n > square:
        square = counter * counter
        counter = counter + 1

    if square > n:
        counter = counter - 2
        square = counter * counter

    print(str(square))

perfect(500)
