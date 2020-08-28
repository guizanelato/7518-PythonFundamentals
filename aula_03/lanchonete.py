#!/usr/bin/python3

"""
Transformar o exercício da lanchonete aplicando a modularização de acordo
com o modelo contido no padrao_script.py 

main: menu [x] e direcionamentos[?]

criar:
    uma função para funcionalidade:
        1- adicionar o lanche [x]
        2- mostrar pedido [x]
        3- consolidar total [x]

"""

def menu():
    op = input(f'Informe a opção desejada:\n'
               f'1- X-Salada(3.50)\n'
               f'2- X Bacon(4.50)\n'
               f'3- X-Tudo(6.00)\n'
               f'4- Mostrar Pedido\n'
               f'5- Total\n'
               f'6- Sair\n') 
    return op

def adicionar_lanche(comanda, opcao_informada):
    """
    Recebe uma opção de lanche contida no cardápio e uma comanda.
    Adiciona na comanda o prato de acordo.

    """
    cardapio = {
            '1': ('X-Salada', 3.50),
            '2': ('X-Bacon', 4.50),
            '3': ('X-Tudo', 6.00),
            'cod': ('Desc', 9999)
            }

    comanda.append(cardapio[opcao_informada])
    #comanda[cardapio[opcao_informada][0]] = cardapio[opcao_informada][1] 
    print("Lanche adicionado com sucesso!")

def mostrar_pedido(comanda, opcao_informada):
    for item in comanda:
        print(f' Lanche: {item[0]} - Preço: {item[1]}') 
    

def total_pedido(comanda, opcao_informada):
    total = 0
    for lanche in comanda:
        total += lanche[1]
    print(f'Total do pedido R${total:.2f}')


def sair(comanda=None, opcao_informada=None):
    exit(0)


### função principal
def main():
    pedido = []
    # comanda = {}
    opcoes = {
        '1':adicionar_lanche,
        '2':adicionar_lanche,
        '3':adicionar_lanche,
        '4':mostrar_pedido,
        '5':total_pedido,
        '6':sair    
    }

    while True: #2
        opcao = menu()
        if opcao in opcoes.keys():
            opcoes[opcao](pedido, opcao)
        else:
            print('Opção Inválida')


### validação __name__

if __name__ == '__main__':
    main()

