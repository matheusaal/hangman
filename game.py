import communication
import support_functions
import main

def game():

    randomChoice = support_functions.randomWordClass()
    secretWord, secretClass = randomChoice[0], randomChoice[1]

    wrongTries = []
    oldTries = []

    leftTries = 6

    mask = support_functions.createMask(secretWord)

    print("\nClass:", secretClass)

    while(True):

        # Verify defeat
        if (leftTries == 0):

            communication.loserMessage()
            print("\n\nThe secret word was:", secretWord)
            break
        
        support_functions.printList(mask)

        currentTry = input("\n\nWhich letter do you choose? ").upper()
    
        if (not currentTry.isalpha()) or (len(currentTry) != 1) or (currentTry in oldTries):

            print("\nYour attempt is invalid! Please, try again.\n")

        else:

        # Right try logic
            if (currentTry in secretWord):

                print("\nWell done! Right try. \n")
                indexLetter = support_functions.findLettersIndex(secretWord, currentTry) # Find all index of a letter in the secret word
                
                for i in indexLetter:

                    mask[i] = currentTry # Change the "_" from the mask to the correct letter
        
                oldTries.append(currentTry) # Add the current try to a list containing all old tries
                
            # Wrong try logic
            elif (currentTry not in secretWord):

                print("\nOoh! What a shame, your try is wrong.\n")

            
                oldTries.append(currentTry) # Add the current try to a list containing all old tries
                wrongTries.append(currentTry) #  Add the current try to a list containing just the wrong tries (to show them later)

                leftTries -= 1 # Calculate the left tries using the size of the wrong tries list
                communication.hangmanDrawing(6 - leftTries) # Draws a hangman using wrong tries amount as a parameter

                if (leftTries > 0):

                    print("You have", leftTries, "tries left.\n")
                    print("Old tries: ", end="")

                    support_functions.printList(wrongTries)

                print("\n")

        
            # Verify victory
            if (mask == support_functions.convertStringToList(secretWord)):

                communication.winnerMessage()
                break