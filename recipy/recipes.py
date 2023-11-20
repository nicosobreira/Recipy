from strings.strings import *
from .utils import askUserInfo, pastaAtual
from terminal import clearTerminal
from .constants import *
import json


# Receita:
#   Nome - Verde
#   Categorias - Roxo
#   Ingredientes - Blue
#   Passos - None


def escolheReceita():
    while True:
        nome = askUserInfo(
            f'Qual é o {colors("nome", style="Blink")} da {"receita à ser editada"}? ')
        if nome in NOMES:
            return NOMES[nome]
        errorMessage('Digite um nome válido')


def novaReceita():
    line('-', 30)
    nome = askUserInfo(
        f'Qual é o {colors("nome", style="Blink")} da {rainbow("nova receita")}? ')
    line('-', 30)
    categorias = perguntaAté('Quais são as categorias? ')
    line('~', 30)
    ingredientes = perguntaAté('Quais são os ingredientes? ')
    passos = editorTexto()

    receita = f"""
        {nome}: {{
        'Categorias': {categorias},
        'Ingredientes': {ingredientes},
        'Passos': {passos}
        }}
        """
    return receita


def editaReceita(receita=dict()):
    def opção():
        while True:
            line('>', 30)
            print('Oque deseja editar')
            for key, item in EDITOR.items():
                print(f'{key} - {item}')
            opção = askUserInfo('>> ').upper()
            if opção in EDITOR.keys():
                return opção
            errorMessage('Digite uma opção válida')
    while True:
        opção = opção()


def mostraReceita(nome_receita, eixo_x=30, eixo_y=30):
    pass


def editorTexto(texto_anterior=['']):
    clearTerminal()
    line('-', 30)
    print(
        f'{colors(">>", "Purple")} {"Digite CTRL + C para parar":^30} {colors("<<", "Purple")}')
    
    if texto_anterior[0] == '':
        texto = []
        index = -1
    else:
        texto = texto_anterior
        for index, linha in enumerate(texto_anterior):
            print(f'{colors(str(index) + ".", style="Dark")} {linha}')

    while True:
        index += 1
        print(colors(str(index) + ".", style="Dark"), end=' ')
        try:
            linha = str(input(''))
            texto.append(linha)
        except KeyboardInterrupt:
            print()
            ic(texto)
            return texto


def perguntaAté(pergunta=''):
    respostas = []

    index = 0
    print('Digite CTRL + C para parar'.center(30))
    print(f'{colors(">>", "Blue")} {pergunta} {colors("<<", "Blue")}'.center(30))
    while True:
        print(colors(str(index) + ".", style="Dark"), end=' ')

        try:
            resposta = str(input('')).strip()
        except KeyboardInterrupt:
            print()
            if len(respostas) != 0:
                for resp in respostas:
                    if resp == '':
                        respostas.pop(respostas.index(resp))
                return respostas
            errorMessage('Coloque pelo menos 1 valor')
        else:
            respostas.append(resposta)
        index += 1
