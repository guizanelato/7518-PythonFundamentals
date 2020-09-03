## Tratamento de Exceções 

def main():
    opcoes = {
        '1': lambda n1,n2: n1+n2,
        '2': lambda n1,n2: n1-n2,
        '3': lambda n1,n2: n1*n2,
        '4': lambda n1,n2: n1**n2,
        '5': lambda n1,n2: n1/n2,
        '6': lambda n1,n2: exit(0)
    }
    
    while True:

        try:
            # trechos de códigos suscetíveis a erro
            ## conexões com banco de dados, requisitoes http, abertura de arquivos....
            ## próprio funcionamento da máquina
            
            with open('n1.txt') as arquivo:
                n1 = float(arquivo.read().strip())
                print(n1)

            with open('n2.txt') as arquivo:
                n2 = float(arquivo.read().strip())
                print(n2)
            escolha = input(f'Informe a operação desejada:\n'
                            f'1- Soma\n' 
                            f'2- Subtração\n'
                            f'3- Multiplicação\n'
                            f'4- Exponenciação\n'
                            f'5- Divisão\n'
                            f'6- Sair\n'
                    )
            
            print(opcoes[escolha](n1,n2))
        
        except ValueError:
            print('Informe apenas Números')
        
        except ZeroDivisionError as err:
            print('Não dividirás por zero')

        except KeyError as err:
            print('Opção inválida:', err)

        except KeyboardInterrupt:
            print('Opção Inválida')

        except FileNotFoundError:
            print('Arquivo não encontrado')

        except EOFError:
            print('apertei crtl + d')

        except Exception as err:
            print('Erro desconhecido', err) 
            # Critical
        else:
            ### executa quando bem sucedido
            print('Operação Efetuada com Sucesso!')
        
        finally:
            # executa independente do sucesso ou fracasso do bloco try
            print('passei por aqui')


    
if __name__ == '__main__':
    main()
