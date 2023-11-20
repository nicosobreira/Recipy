def clearTerminal():
    from os import system, name

    if name == 'posix':  # For Unix/Linux/Mac
        system('clear')
    elif name == 'nt':  # For Windows
        system('cls')
    else:
        pass


def exitProgram():
    from strings.strings import boxList
    from sys import exit

    MENSAGEM = [
        '       ',
        '|     |',
        '|     |',
        '=_____=',
        '       '
    ]
    clearTerminal()
    boxList(MENSAGEM, 13, 2)
    print('Volte sempre!'.center(15))
    exit()
