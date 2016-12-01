import random
numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def shuffle(numberlist):

    for x in range(0,10):
        index = random.randint(0,((len(numberlist) -1)))
        pointer = numberlist[x]
        numberlist[x] = numberlist[index]
        numberlist[index] = pointer

    print(str(numberlist))

shuffle(numberlist)


        
        
                               
                                  
                               

    
