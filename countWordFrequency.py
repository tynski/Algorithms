def countWordFrequency(wordList):
    wordNameandCount = []
    for newWord in wordList:
        for existingWord in wordNameandCount:
            if newWord == existingWord[0]:
                existingWord[1] += 1
                break
        else:
            wordNameandCount.append([newWord,1])
    return wordNameandCount
