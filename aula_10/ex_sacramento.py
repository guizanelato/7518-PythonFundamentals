
# carregar o arquivo
with open('data/sacramento.csv', 'rt') as f:
    imoveis = f.readlines()


lista_filtro = [ imoveis[x] for x in range(1,len(imoveis)) if int(imoveis[x].split(',')[9]) > 10000 ]

def filtro(lista):
    resultado = []
    for elemento in lista:
        if int(elemento.split(',')[9]) > 10000:
            resultado.append(elemento)
    return resultado


