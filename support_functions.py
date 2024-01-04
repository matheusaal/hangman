import communication

def convertStringToList(word):

    listWord = []

    for i in range(len(word)):
    
        listWord.append(word[i])

    return listWord

def findLettersIndex(word, letter):

    indexList = []
    word = convertStringToList(word)

    while (letter in word):

        currentIndex = word.index(letter)
        indexList.append(currentIndex)
        word[currentIndex] = "*"

    return indexList

def createMask(word):

    mask = []

    for i in range(len(word)):

        mask.append("_")
        
    return mask

def printList(list):

    for i in range(len(list)):

        print(list[i], end="\t")

    


