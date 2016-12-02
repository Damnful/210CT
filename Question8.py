def remove_Vowel(string, x=0):
    vowels = ("i", "e", "o", "u", "a")
    if x < 0 or x > 4:
        print(str(string))
        # cycles through function until every item in vowels
        # list has been removed
    else:
        remove_Vowel(string.replace(vowels[x], ""), x+1)
        # if index of vowels is present in string, replace
        # with nothing. iterates through list with x+1
 
remove_Vowel("beautiful")
