#!/usr/bin/python3

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
