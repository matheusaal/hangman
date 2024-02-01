import communication
import game

def main():

    communication.openingMessage()

    while(True):

        option = communication.initialMenu()

        if (option == "1"):

            game.game()
        
        if (option == "2"):

            exit()

if __name__ == "__main__":

    main()
