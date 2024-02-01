def openingMessage():

    print("""
             _    _                                         
            | |  | |                                        
            | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
            |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
            | |  | | (_| | | | | (_| | | | | | | (_| | | | |
            |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                __/ |                      
                                |___/     
    """)
                    


def initialMenu():

    print("\nWhich option would you like to take?\n")

    print("1: Play a new game\n")

    print("2: Exit\n")

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
    
    print("Wow, you lost the game!\n")
    

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


def hangmanDrawing(mistakes):

    
    if (mistakes == 1):

        print("\t  _______       ")
        print("\t |       |      ")
        print("\t |      (_)")
        print("\t |       ")
        print("\t |       ")
        print("\t |       ")
        print("\t |              ")
        print("\t_|___           \n")
        
    if (mistakes == 2):

        print("\t  _______       ")
        print("\t |       |      ")
        print("\t |      (_)")
        print("\t |       |")
        print("\t |       ")
        print("\t |       ")
        print("\t |              ")
        print("\t_|___           \n")

    if (mistakes == 3):

        print("\t  _______       ")
        print("\t |       |      ")
        print("\t |      (_)")
        print("\t |      \\|")
        print("\t |       ")
        print("\t |       ")
        print("\t |              ")
        print("\t_|___           \n")
        

    if (mistakes == 4):

        print("\t  _______       ")
        print("\t |       |      ")
        print("\t |      (_)")
        print("\t |      \\|/")
        print("\t |       ")
        print("\t |       ")
        print("\t |              ")
        print("\t_|___           \n")
        
    
    if (mistakes == 5):

        print("\t  _______       ")
        print("\t |       |      ")
        print("\t |      (_)")
        print("\t |      \\|/")
        print("\t |       |")
        print("\t |      /")
        print("\t |              ")
        print("\t_|___           \n")
        

    if (mistakes == 6):

        print("\t  _______       ")
        print("\t |       |      ")
        print("\t |      (_)")
        print("\t |      \\|/")
        print("\t |       |")
        print("\t |      / \\")
        print("\t |              ")
        print("\t_|___           \n")