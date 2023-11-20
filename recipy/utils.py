from terminal import *
from strings.strings import errorMessage


def askUserInfo(pergunta='', tipo='str'):
    '''Ask the user for some info

    Args:
        pergunta (str, optional): Qual é a pergunta que será feita? Defaults to ''.
        tipo (str, optional): tipo da variável a ser perguntada. Defaults to 'str'.

    Returns:
        str, int or float
    '''

    while True:
        try:
            resposta = str(input(pergunta)).strip()
            match tipo:
                case 'str':
                    pass
                case 'int':
                    resposta = int(resposta)
                case 'float':
                    resposta = float(resposta)
        except KeyboardInterrupt:
            exitProgram()
        except ValueError:
            errorMessage(f'Digite um valor do tipo "{tipo}"')
        else:
            return resposta


def pastaAtual():
    from os import getcwd

    return getcwd()
