def binary_search(array,target1,target2):
    print("Search for number within interval: " + str(target1) + "-" + str(target2))
    print(array)
    
    while target1 != target2 + 1:
        first = 0
        last = len(array) - 1
        found = False
        
        while first <= last and found == False:
            midpoint = (first + last) // 2
            if array[midpoint] == target1:
                found = True
            else:
                if target1 < array[midpoint]:
                    last = midpoint -1
                else:
                    first = midpoint +1

        if found:
            return str(target1) + " found"
        else:
            print(str(target1) + " not found")
            if target1 == target2:
                return false
            else:
                target1 += 1
                      
print(binary_search([10,20,30,40,50,60,70,80,90],7,10))
