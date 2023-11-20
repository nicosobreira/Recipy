from strings.strings import *
from .utils import askUserInfo
from .constants import *


def menu():
    while True:
        boxList(MENU.values(), 28, 1)
        resposta = askUserInfo(
            input('Qual é sua escolha? [1º letra ou posição] ')).upper()
        if resposta in MENU.keys():
            break
        else:
            errorMessage('Digite um valor válido. EX.: 1 ou N')
