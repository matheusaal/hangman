import communication
import support_functions

def game():

    secretWord = "Fish"
    secretWordClass = "Food"
    wrongTries = []
    oldTries = []
    mask = support_functions.createMask(secretWord)

    print("\nClass:", secretWordClass, "\n")

    while(True):

        support_functions.printList(mask)

        if (wrongTries == 6):

            communication.loserMessage()
            communication.initialMenu()

            break

        currentTry = input("Which letter do you choose? ")

        if (currentTry not in oldTries and currentTry in secretWord):

            print("\n\nWell done! Right try. \n")
            indexLetter = support_functions.findLettersIndex(secretWord, currentTry)
            
            for i in indexLetter:

                mask[i] = currentTry
    
            oldTries.append(currentTry)
            

        elif (currentTry not in oldTries and currentTry not in secretWord):

            print("\nOoh! What a shame, your try is wrong.\n")

        
            oldTries.append(currentTry)
            wrongTries.append(currentTry)

            leftTries = 6 - len(wrongTries)

            communication.hangmanDrawing(len(wrongTries))

            print("You have", leftTries, "tries left.\n")
            print("Old tries: ", end="")

            support_functions.printList(wrongTries)

            print("\n")

        else:

            print("\nYour attempt is invalid! Please, try again.")

        if (mask == support_functions.convertStringToList(secretWord)):

            communication.winnerMessage()
            communication.initialMenu()
            
            break