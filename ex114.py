import webbrowser
try:
    webbrowser.open('https://www.palpitedigital.com/acessar-paginas-via-codigo-python/')
except (SyntaxError):
    print('Site não encontrado')
else:
    print('Site encontrado')