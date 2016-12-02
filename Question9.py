def binary_search(array,target1,target2):
    print("Search in array for number within interval: " + str(target1) + " - " + str(target2))
    print(array)
 
    while target1 != target2 + 1:
    # this is the loop for incrementing the value that we are searching for
        first = 0
        last = len(array) - 1
        # -1 is needed due to index range
        found = False
 
        while first <= last and found == False:
        # this is the main loop for the binary search to see if current value is in the array
            midpoint = (first + last) // 2
            # midpoint is the key to the search as it is divide and conquer
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
                # increment the target value if previous value not found in array
 
print(binary_search([10,20,30,40,50,60,70,80,90],7,10))
