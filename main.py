# Chat con Emojis en Python

texto = input(">")

seguuirChatenado = True

while seguuirChatenado:
    texto = input(">")
    if texto == 'salir':
        seguuirChatenado = False
    texto = texto.replace(':)', '😊')
    texto = texto.replace(':(', '😢')
    texto = texto.replace(':D', '😀')
    texto = texto.replace(':P', '😛')
    texto = texto.replace(':O', '😲')
    texto = texto.replace(':*', '😘')
    texto = texto.replace(';)', '😉')
    print(texto)
