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

def game():

    secretWord = "sardinha"
    secretWordClass = "comida"
    wrongTries = 0
    oldTries = []
    mask = createMask(secretWord)

    while(True):

        print("\nClass: ", secretWordClass, "\n")

        printList(mask)

        if (wrongTries == 6):

            communication.loserMessage()
            communication.initialMenu()

            break

        currentTry = input("Which letter do you choose? ")

        if (currentTry not in oldTries and currentTry in secretWord):

            print("\n\nWell done! Right try. \n")
            indexLetter = findLettersIndex(secretWord, currentTry)
            
            for i in indexLetter:

                mask[i] = currentTry
    
            oldTries.append(currentTry)
            

        elif (currentTry not in oldTries and currentTry not in secretWord):

            print("\nOoh! What a shame, your try is wrong.\n")

            wrongTries += 1

            oldTries.append(currentTry)
            communication.hangingManDrawing(wrongTries)
            print("Old tries: ", end="")
            printList(oldTries)
            print("")

        else:

            print("\nYour attempt is invalid! Please, try again.")

        if (mask == convertStringToList(secretWord)):

            communication.winnerMessage()
            communication.initialMenu()
            break

def main():
    
    communication.openingMessage()

    option = communication.initialMenu()

    if (option == "1"):

        game()
    
    if (option == "2"):

        pass

    if (option == "3"):

        exit()


main()

'''

Falta para finalizar:

- Banco de dados
- Caracteres especiais: ã, ê, etc
- Sensitive case
- Quantidade de chances
- Exibir tentativas restantes
- Resolver espaçamento lista de tentativas

'''