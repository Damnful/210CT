def find_maximum_subsequence(sequence):
    subsequenceList = []
    currentSubsequence = []
    maximumSubsequence = []
    last = 0

    for integer in sequence:
        if integer <= last:
            subsequenceList.append(currentSubsequence)
            currentSubsequence = []
        currentSubsequence.append(integer)
        last = integer

    subsequenceList.append(currentSubsequence)
    
    for subsequence in subsequenceList:
        if len(maximumSubsequence) < len(subsequenceList):
            maximumSubsequence = subsequence
    print(str(maximumSubsequence))
    
find_maximum_subsequence([0,1,3,4,7,3,4,6,7,1,4,5,9,2,4,5])      
