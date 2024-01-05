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

        # Verify defeat
        if (wrongTries == 6):

            communication.loserMessage()
            communication.initialMenu()

            break

        currentTry = input("Which letter do you choose? ")

        # Right try logic
        if (currentTry not in oldTries and currentTry in secretWord):

            print("\n\nWell done! Right try. \n")
            indexLetter = support_functions.findLettersIndex(secretWord, currentTry) # Find all index of a letter in the secret word
            
            for i in indexLetter:

                mask[i] = currentTry # Change the "_" from the mask to the correct letter
    
            oldTries.append(currentTry) # Add the current try to a list containing all old tries
            
        # Wrong try logic
        elif (currentTry not in oldTries and currentTry not in secretWord):

            print("\nOoh! What a shame, your try is wrong.\n")

        
            oldTries.append(currentTry) # Add the current try to a list containing all old tries
            wrongTries.append(currentTry) #  Add the current try to a list containing just the wrong tries (to show them later)

            leftTries = 6 - len(wrongTries) # Calculate the left tries using the size of the wrong tries list
            wrongTriesQuantity = len(wrongTries) # Calculate the wrong tries amount using the size of the wrong tries list

            communication.hangmanDrawing(wrongTriesQuantity) # Draws a hangman using wrong tries amount as a parameter

            print("You have", leftTries, "tries left.\n")
            print("Old tries: ", end="")

            support_functions.printList(wrongTries)

            print("\n")

        else:

            print("\nYour attempt is invalid! Please, try again.")

        # Verify victory
        if (mask == support_functions.convertStringToList(secretWord)):

            communication.winnerMessage()
            communication.initialMenu()
            
            break