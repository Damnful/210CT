def binary_search(array,target):
    print(array)
    first = 0
    last = len(array) - 1
    found = False
    
    while first <= last and found == False:
        midpoint = (first + last) // 2
        if array[midpoint] == target:
            found = True
        else:
            if target < array[midpoint]:
                last = midpoint -1
            else:
                first = midpoint +1

    if found: return str(target) + " found"
    else: return "not found"
                      
print(binary_search([10,20,30,40,50,60,70,80,90],10))
