def find_maximum_subsequence(sequence):
    subsequenceList = []
    currentSubsequence = []
    maximumSubsequence = []
    last = 0
 
    for integer in sequence:
        if integer <= last:
        # basically, if the next value continues the increasing subsequence
            subsequenceList.append(currentSubsequence)
            # this is a list of lists, holding all the maximum increasing seqs
            currentSubsequence = []
        currentSubsequence.append(integer)
        last = integer
        # last is a comparison variable
 
    subsequenceList.append(currentSubsequence)
 
    for subsequence in subsequenceList:
        # iterates through list of lists to find largest list 
        if len(maximumSubsequence) < len(subsequenceList):
            maximumSubsequence = subsequence
    print(str(maximumSubsequence))
 
find_maximum_subsequence([0,1,3,4,7,3,4,6,7,1,4,5,9,2,4,5])
