import communication
import random

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

        print(list[i], end=" ")

def randomWordClass():

    with open('randomWords.txt', 'r', encoding='utf-8') as wordsArchive:

        lines = wordsArchive.readlines()

        chosenLine = random.choice(lines)
    
    secretWordClass = chosenLine.split(",")
    secretWordClass[0] = secretWordClass[0].upper()
    secretWordClass[1] = secretWordClass[1].strip()

    return secretWordClass


        
        


