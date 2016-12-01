def split_sentence(sentence):
    
    reversedSentence = []
    splitSentence = sentence.split(" ")
    for word in reversed(splitSentence):
        reversedSentence.append(word)

    for x in range(0, len(reversedSentence)):
        print(reversedSentence[x], end=" ")


split_sentence('This is awesome')
