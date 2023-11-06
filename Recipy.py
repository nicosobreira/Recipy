from icecream import ic, install
from strings.strings import *
from files.editor import *
import json

install()


# Receita:
#   nome - Verde
#   categoria - Roxo
#   ingredientes - Blue
#   passos - None


def main():
    resposta = menu()
    if resposta == 'S':
        exitProgram()

    with open("receitas.json", "r") as file:
        RECEITAS = json.load(file)

    RECEITAS_LIST = [receita for receita in RECEITAS.keys()]

    clearTerminal()
    match resposta:
        case 'N' | '1':
            line('-', 30)
            nome = str(input(
                f'Qual é o {colors("nome", "Blue", style="Blink")} da {rainbow("nova receita")}? '))

            line('-', 30)
            print(
                f'{colors(">>", "Blue")} Digite 0 para parar {colors("<<", "Blue")}'.center(30))
            categorias = perguntaAté('Quais são as categorias? ')
            line('-', 30)
            ingredientes = perguntaAté('Quais são os ingredientes? ')

            line('-', 30)
            print(
                f'{colors(">>", "Purple")} Digite ENTER 2x para parar {colors("<<", "Purple")}'.center(30))
            passos = editorTexto()
        case 'E' | '2':
            while True:
                boxList(RECEITAS_LIST, 34, 0)
                nome = str(input(f'Escolha uma das {colors("receita", "Green")}: ')).capitalize()
                if nome in RECEITAS_LIST:
                    break
                errorMessage('Digite um nome de receita')
            
            opção = str(input('Oque quer editar? '))


def menu():
    while True:
        boxList(MENU.values(), 28, 1)
        resposta = str(input('Qual é sua escolha? [1º letra ou posição] ')).strip().upper()
        if resposta in MENU.keys():
            return resposta
        else:
            errorMessage('Digite um valor válido. EX.: 1 ou N')


def perguntaAté(pergunta, até='0'):
    respostas = []

    while True:
        resposta = str(input(pergunta))
        if resposta == até:
            if len(respostas) != 0:
                return respostas
            else:
                errorMessage('Pelo meno 1 valor')
        if resposta == '':
            errorMessage('Digite alguma coisa')
        else:
            respostas.append(resposta)


if '__main__' == __name__:
    main()
