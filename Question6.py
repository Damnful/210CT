def split_sentence(sentence):
    
    reversedSentence = [] 
    # empty sentence to append to
    splitSentence = sentence.split(" ")
    # splits the words up in the sentence
    
    for word in reversed(splitSentence):
        reversedSentence.append(word)
        # for every word in the original sentence, we append to the new sentence

    for x in range(0, len(reversedSentence)):
        print(reversedSentence[x], end=" ")
        # this is just used to print the reversed sentence in a nice format

split_sentence('This is awesome')
