#!/usr/bin/python3

import lanchonete

### função principal
def main():
    pedido = []
    # comanda = {}
    opcoes = {
        '1':lanchonete.adicionar_lanche,
        '2':lanchonete.adicionar_lanche,
        '3':lanchonete.adicionar_lanche,
        '4':lanchonete.mostrar_pedido,
        '5':lanchonete.total_pedido,
        '6':lanchonete.sair    
    }

    while True: #2
        opcao = lanchonete.menu()
        if opcao in opcoes.keys():
            opcoes[opcao](pedido, opcao)
        else:
            print('Opção Inválida')


### validação __name__

if __name__ == '__main__':
    main()

