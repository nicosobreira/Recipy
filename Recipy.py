from icecream import ic, install
from strings.strings import *
from recipy import *
from terminal import *
import json
install()


def main():
    with open(utils.pastaAtual() + '/data/receitas.json') as file_receita:
        RECEITAS = json.load(file_receita)
        constants.NOMES = [nome for nome in RECEITAS.keys()]
    while True:
        resposta = menu()
        clearTerminal()
        match resposta:
            case 'S' | '0':
                exitProgram()
            case 'N' | '1':
                nova_receita = recipes.novaReceita()
            case 'E' | '2':
                receita = recipes.escolheReceita()
                receita_editada = recipes.editaReceita(receita)
                if receita_editada != None:
                    pass


if __name__ == "__main__":
    main()
