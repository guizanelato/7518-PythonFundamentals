# Arquivos


## Utilizando contextos (with) 
with open('arquivo.txt') as arquivo:
    conteudo = arquivo.readlines()
    for linha in conteudo:
        print(linha, end='')


exit()
## Abertura de arquivos com a função open()

arquivo = open('arquivo.txt', 'a')
conteudo = 'esta é a quinta linha\n'
mascara =  '\n' +  conteudo
arquivo.write(conteudo)
arquivo.close

# conteudo = arquivo.read() # lê um arquivo como um todo (ou até o limite) e transforma em uma string
# conteudo = arquivo.readline(100000) # unidade de leitura passa ser linhas e não caracteres 
# conteudo = arquivo.readlines()  # realiza a leitura e armazena cada linha em uma lista

##### 

#### Modos de abertura

### open('nome_do_arquivo.ext', 'modo_de_abertura')

## 'r': abre o arquivo no modo de leitura, não é possível realizar alterações 
## 'w': abre o arquivo no modo de escrita, sobrescrevendo o arquivo de origem (truncate) 
## 'x': cria um novo arquivo e permite a escrita; caso o arquivo existir ele retorna um erro
## 'a': abre um arquivo para escrita, ele posiciona o cursor ao final do arquivo

#### abertura do arquivo para leitura 
##### carrega informações  
#### manipulação dos dados -> preservar o conteúdo 
#### realizar a escrita (persistência)
##### abre no modo de escrita




