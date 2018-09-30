def countWordFrequency(wordList):
    wordNameandCount = {}
    for newWord in wordList:
      if newWord in wordNameandCount:
        wordNameandCount[newWord] += 1     
      else:
        wordNameandCount[newWord] = 1
    return wordNameandCount.items()
