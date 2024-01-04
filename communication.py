def openingMessage():

    print("\n*****************************\n\n")
    print("  Welcome to Hangman Game!\n")
    print("  Created by Matheus Avila.\n\n")
    print("*****************************\n")


def initialMenu():

    print("\nWhich option would you like to take?\n")

    print("1: Play a new game\n")

    print("2: Register a new word and the respective class\n")

    print("3: Exit\n")

    return input("")


def winnerMessage():

    print("Congratulations, you won the game!\n")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def loserMessage():
    
    print("Wow, you lost the game!")
    print("The secret word was: ")

    print("    _______________         ")
    print("   /               \\       ")
    print("  /                 \\      ")
    print("//                   \\/\\  ")
    print("\\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \\__      XXX      __/     ")
    print("   |\\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \\_             _/       ")
    print("     \\_         _/         ")
    print("       \\_______/           ")


def hangingManDrawing(mistakes):

    
    if (mistakes == 1):

        print("\t  _______       ")
        print("\t |       |      ")
        print("\t |      (_)")
        print("\t |       ")
        print("\t |       ")
        print("\t |       ")
        print("\t |              ")
        print("\t_|___           \n\n")
        
    if (mistakes == 2):

        print("\t  _______       ")
        print("\t |       |      ")
        print("\t |      (_)")
        print("\t |       |")
        print("\t |       ")
        print("\t |       ")
        print("\t |              ")
        print("\t_|___           \n\n")

    if (mistakes == 3):

        print("\t  _______       ")
        print("\t |       |      ")
        print("\t |      (_)")
        print("\t |      \\|")
        print("\t |       ")
        print("\t |       ")
        print("\t |              ")
        print("\t_|___           \n\n")
        

    if (mistakes == 4):

        print("\t  _______       ")
        print("\t |       |      ")
        print("\t |      (_)")
        print("\t |      \\|/")
        print("\t |       ")
        print("\t |       ")
        print("\t |              ")
        print("\t_|___           \n\n")
        
    
    if (mistakes == 5):

        print("\t  _______       ")
        print("\t |       |      ")
        print("\t |      (_)")
        print("\t |      \\|/")
        print("\t |       |")
        print("\t |      /")
        print("\t |              ")
        print("\t_|___           \n\n")
        

    if (mistakes == 6):

        print("\t  _______       ")
        print("\t |       |      ")
        print("\t |      (_)")
        print("\t |      \\|/")
        print("\t |       |")
        print("\t |      / \\")
        print("\t |              ")
        print("\t_|___           \n\n")