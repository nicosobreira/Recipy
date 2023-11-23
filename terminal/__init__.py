def clearTerminal():
    from os import system, name

    if name == 'posix':  # For Unix/Linux/Mac
        system('clear')
    elif name == 'nt':  # For Windows
        system('cls')
    else:
        pass


def exitProgram():
    from strings.strings import colors, lineDark
    from sys import exit

    MENSAGEM = [
        colors('|     |', 'Green'),
        colors('|     |', 'Green'),
        colors('=_____=', 'Blue')
    ]
    clearTerminal()
    print(' ' * 7, end='')
    print(f"{colors('-', style='Dark') * 15}")
    for mensagem in MENSAGEM:
        print(mensagem.center(41))
    print('Volte sempre!'.center(30))
    print(' ' * 7, end='')
    print(f"{colors('-', style='Dark') * 15}")
    exit()
