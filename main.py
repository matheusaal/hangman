import communication
import game

def main():
    
    communication.openingMessage()

    option = communication.initialMenu()

    if (option == "1"):

        game.game()
    
    if (option == "2"):

        pass

    if (option == "3"):

        exit()


main()

'''

Falta para finalizar:

- Banco de dados
- Sensitive case
- Resolver espaçamento lista de tentativas

'''