from icecream import ic, install
from strings.strings import *
from recipy import *
from terminal import *
import json
install()


def main():
    while True:
        with open('data/teste.json') as file_receita:
            try:
                receitas = json.load(file_receita)
            except:
                receitas = {}
            else:
                constants.NOMES = [nome for nome in receitas.keys()]
        clearTerminal()
        resposta = utils.askOptions(constants.MENU, constants.MENU_COLORS)
        clearTerminal()
        match resposta:
            case 'S' | '4':
                exitProgram()
            case 'M' | '0':
                pass
            case 'N' | '1':
                receita_usr = recipes.novaReceita()
                receitas.update(receita_usr)
                with open('data/teste.json', 'w', encoding='utf-8') as file_receita:
                    json.dump(receitas, file_receita, indent=4)
            case 'E' | '2':
                nome_antigo = editor.escolheReceita()
                receita_usr = recipes.editaReceita(receitas[nome_antigo])
                receitas.pop(nome_antigo); receitas.update(receita_usr)
                with open('data/teste.json', 'w', encoding='utf-8') as file_receita:
                    json.dump(receitas, file_receita, indent=4, ensure_ascii=True)
            case 'X' | '3':
                pass


if __name__ == "__main__":
    main()
