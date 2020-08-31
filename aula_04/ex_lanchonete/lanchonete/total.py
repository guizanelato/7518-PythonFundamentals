#/usr/bin/python3

def total_pedido(comanda, opcao_informada):
    total = 0
    for lanche in comanda:
        total += lanche[1]
    print(f'Total do pedido R${total:.2f}')
