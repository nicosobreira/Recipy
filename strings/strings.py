from strings.constraints import *


def errorMessage(message):
    message = message.split()
    boxList(message, 35, 3)


def line(type='-', length=30):
    print(type * length)


def showText(text, type='-', length=30):
    print(type * length)
    print(text.center(length))
    print(type * length)


def colors(text, color='None', background='None', style='None'):
    '''Generate a text with colors

    Color and Background [options]:
        Black, Red, Green, Orange, Yellow, Blue, Cyan, Gray, None

    Style [options]:
        None, Bold, Dark, Italic, Underline, Blink, Negative, Risk
    '''

    color_code = f'\033[{STYLE[style]};{COLORS[color] + 30};{COLORS[background] + 40}m'
    return f'{color_code}{text}\033[m'


def randomColor(text):
    from random import choice

    color = choice(COLORS_LIST)
    return colors(text, color)


def rainbow(text):
    format_text = ''
    count = 0

    for character in text:
        if character == ' ':
            format_text += ' '
        else:
            format_text += colors(character, RAINBOW[count])
            if count == len(RAINBOW) - 1:
                count = 0
            else:
                count += 1
    return format_text


"""
def formatMoney(money):
    str_money = f'{money:.2f}'
    return cfg.TYPE_MONEY + str_money
"""


def boxList(lista, length, type=0):
    def customLine():
        print(colors(BOXES[type]['corner'], BOXES[type]['colors'][1]), end='')
        print(rainbow(BOXES[type]['line'] * length), end='')
        print(colors(BOXES[type]['corner'], BOXES[type]['colors'][1]), end='')
        print()

    length -= 2
    customLine()
    for elemento in lista:
        print(colors(BOXES[type]['column_1'], style="Dark"), end='')
        print(
            colors(str(elemento).center(length), BOXES[type]['colors'][0]), end=''
        )
        print(colors(BOXES[type]['column_2'], style="Dark"), end='')
        print()
    customLine()


def clearTerminal():
    from os import system, name

    if name == 'posix':  # For Unix/Linux/Mac
        system('clear')
    elif name == 'nt':  # For Windows
        system('cls')
    else:
        pass


def exitProgram():
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
    exit()