def editorTexto(texto_anterior=''):
    texto = ''

    while True:
        linha = str(input(texto_anterior))
        if linha == '':
            break
        texto += linha + '\n'
    return texto
