from strings.strings import *
from .constants import *
from .utils import *


def escolheReceita():
    while True:
        lineDark('<', 40)
        print(
            f'Qual é o {colors("nome", "Blue")} da receita? '.center(55))
        lineDark('>', 40)
        nome = askUserInfo(
            f'>> Qual é o nome da receita? ')
        if nome in NOMES:
            return nome
        errorMessage('Digite um nome válido')


def editaAté(mensagem='', lista=[]):
    from time import sleep
    while True:
        clearTerminal()
        line('~', 45)
        print(colors(mensagem, 'Purple', style='Bold').center(55))
        line('>', 45)
        print(f'CTRL + C para parar'.center(45))
        print(f'Digite novamente para excluir'.center(45))
        print(f'Você também pode digitar o índex ;)'.center(45))
        line('<', 45)

        mostraLista(lista)
        lineDark('-', 30)
        try:
            edição = input('>> ').strip()
        except KeyboardInterrupt:
            for elemento in lista:
                if elemento == '':
                    lista.remove(elemento)
            return lista
        try:
            edição = int(edição)
        except ValueError:
            if edição in lista:
                lista.remove(edição)
            else:
                lista.append(edição)
        else:
            if edição in range(len(lista)):
                lista.pop(edição)
            else:
                errorMessage('Digite um índex válido')
                sleep(1)


def editorTexto(texto_anterior=['']):
    clearTerminal()
    print('Editor de Texto'.center(45))
    lineDark('>', 45)
    print(
        f'{colors(">>", "Purple")} {"Digite CTRL + C para parar":^45} {colors("<<", "Purple")}')
    lineDark('<', 45)

    if texto_anterior[0] == '':
        texto = []
        index = -1
    else:
        texto = texto_anterior
        mostraLista(texto_anterior)

    while True:
        index += 1
        print(colors(str(index) + ".", style="Dark"), end=' ')
        try:
            linha = str(input(''))
            texto.append(linha)
        except KeyboardInterrupt:
            print()
            return texto


def mostraLista(lista=[]):
    for index, elemento in enumerate(lista):
        print(colors(str(index) + '.', style='Dark'), elemento)


def continuarReceita():
    lineDark('-', 30)
    print('Deseja continuar?')
    continuação = askUserInfo('>> [S/N] ').upper()
    if continuação in 'SN':
        if continuação == 'S':
            return True
        else:
            return False
    errorMessage('Digite uma opção válida')
