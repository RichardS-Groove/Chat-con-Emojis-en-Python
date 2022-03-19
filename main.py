# Chat con Emojis en Python

texto = input(">")

seguirChatenado = True

while seguirChatenado:
    texto = input(">")
    if texto == 'salir':
        seguirChatenado = False
    texto = texto.replace(':)', '😊')
    texto = texto.replace(':(', '😢')
    texto = texto.replace(':D', '😀')
    texto = texto.replace(':P', '😛')
    texto = texto.replace(':O', '😲')
    texto = texto.replace(':*', '😘')
    texto = texto.replace(';)', '😉')
    print(texto)
