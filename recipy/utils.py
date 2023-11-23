from terminal import *
from strings.strings import *


def askOptions(options={}, colors_list=[]):
    while True:
        lineDark('>', 30)
        color_index = 0
        for key, value in options.items():
            print(colors("| ", colors_list[color_index], style='Dark'), end='')
            print(f'{colors(key, colors_list[color_index], style="Bold")} ~ {value}'.center(39), end='')
            print(colors(" |", colors_list[color_index], style='Dark'), end='')
            print()
            color_index += 1
        lineDark('<', 30)
        resposta = askUserInfo(
            ('Qual é sua escolha? ')).upper()
        if resposta in options.keys():
            return resposta
        else:
            errorMessage('Digite um valor válido')


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
