#!/usr/bin/python3


def mostrar_pedido(comanda, opcao_informada):
    for item in comanda:
        print(f' Lanche: {item[0]} - Preço: {item[1]}') 
