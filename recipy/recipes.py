from strings.strings import *
from .utils import askUserInfo
from terminal import clearTerminal
from .constants import *
from .editor import *
import json


def novaReceita():
    while True:
        lineDark('<', 40)
        print(
            f'Qual é o {colors("nome", "Yellow")} da nova receita? '.center(55))
        lineDark('>', 40)
        nome = askUserInfo('>> ')
        if nome not in NOMES:
            break
        errorMessage('Nome repetido! Digite outro')
        clearTerminal()

    categorias = editaAté('Quais são as categorias? ', [])
    ingredientes = editaAté('Quais são os ingredientes? ', [])
    passos = editorTexto()

    receita = {nome: {
    'Nome': nome,
    'Categorias': categorias,
    'Ingredientes': ingredientes,
    'Passos': passos
    }}
    str_receita = json.dumps(receita)
    print(receita)
    continuação = continuarReceita()
    if continuação:
        return receita
    return None


def editaReceita(receita={}):
    def editar():
        clearTerminal()
        while True:
            lineDark('>', 30)
            print(colors(nome, style='Bold').center(40))
            lineDark('<', 30)
            print(f'Oque deseja editar')
            print(f'{colors("CTRL", "Blue")} + {colors("C", "Blue")} para sair')
            line('-', 30)
            for key, item in EDITOR.items():
                print(f'{colors(key, "Blue")}. {item}')
            try:
                opção = input('>> ').strip().upper()
            except KeyboardInterrupt:
                return None
            if opção in EDITOR.keys():
                return opção
            errorMessage('Digite uma opção válida')

    nome = receita['Nome']
    categorias = receita['Categorias']
    ingredientes = receita['Ingredientes']
    passos = receita['Passos']
    while True:
        opção = editar()
        match opção:
            case None:
                break
            case 'N':
                line('~', 30)
                nome = askUserInfo(f'Qual é o novo {colors("nome", "Blue")} para "{nome}"? ')
            case 'C':
                categorias = editaAté('Categorias', categorias)
            case 'I':
                ingredientes = editaAté('Ingredientes', ingredientes)
            case 'P':
                passos = editorTexto(passos)
    receita = {nome: {
    'Nome': nome,
    'Categorias': categorias,
    'Ingredientes': ingredientes,
    'Passos': passos
    }
    }
    str_receita = json.dumps(receita)
    print(receita)
    continuação = continuarReceita()
    if continuação:
        return receita
    return None


def mostraReceita(receita={}):
    pass
