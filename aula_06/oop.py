#### Orientação à Objetos


#### [x] Abstração
#### [x] Encapsulamento
#### [x] Herança
#### [x] Polimorfismo

import random
import time

class DancaDasCadeiras:
    def __init__(self):
        self._num_cadeiras = 0
        self._participantes = []
        self._num_participantes = 0
        self._ativo = False
    
    def _iniciarDisputa(self):
        self._ativo = True

    def _definirNumeroDeCadeiras(self):
        self._num_cadeiras = self._num_participantes - 1 

    def _removerParticipante(self):
        indice = random.randint(0,self._num_participantes-1)
        perdedor = self._participantes[indice]
        del self._participantes[indice]
        self._num_participantes -= 1
        return perdedor

    def _removerCadeira(self, num_cadeiras=1):
        self._num_cadeiras -= num_cadeiras

    def _indicarVencedor(self):
        return self._participantes[0]
    
    def _adicionaParticipantes(self, nome_jogador):
        self._participantes.append(nome_jogador)
        self._num_participantes += 1
    
    def _enunciaParticipantes(self):
        print('Os participantes do jogo são:')
        for participante in self._participantes:
            print(participante)

    def _encerrarDisputa(self):
        if self._num_participantes == 1:
            self._ativo = False
            return True
        return False

    def _rodada(self):
        print('-----------------------------------------')
        #### inicio a música
        print("Música rolando....!!!")
        time.sleep(2)

        #### paro a musica
        print("Música Parou!")
        time.sleep(1)

        #### movimentação dos jogadores
        print("jogadores se movimentam!")
        time.sleep(0.5)

        #### remove o participante que não conseguiu sentar
        print(f"o jogador {self._removerParticipante()} saiu do jogo!")
        
        #### removemos uma cadeira
        self._removerCadeira()

        #### verifica se ainda o jogo está ativo
        if self._encerrarDisputa():
            print("Fim de Jogo!")

    def novoJogo(self):
        #### Adicionar participantes 
        lista_nomes = [
                'Joana',
                'Felipe',
                'Esther',
                'Pedro',
                'Hector',
                'Julio',
                'Caio',
                'Brian',
                'Fernanda',
                'Juliana'
                ]

        for indice in range(0,random.randint(2,len(lista_nomes))):
            self._adicionaParticipantes(lista_nomes[indice])
        #### Apresentar jogadores
        self._enunciaParticipantes()

        #### Colocar as cadeiras em jogo...
        self._definirNumeroDeCadeiras()

        #### Ativar o jogo
        self._iniciarDisputa()

        #### Iniciar rodadas:
        while self._ativo == True:
            self._rodada()
        #### Jogo encerrado
        print(f"O jogador {self._indicarVencedor()} venceu!")
        

class NovoJogoDasCadeiras(DancaDasCadeiras):
    def verificarQuantidadeParticipantes(self):
        return self._num_participantes


### Organização
### Representação de contextos reais
### Generalização 

class Pessoa:

    def __init__(s,  
                 cpf='111111', 
                 nome='Teste',
                 data_nasc='99/99/9999',
                 cel = '99999-9999',
                 idade=99):

        s.cpf = '' # atributos <-> variáveis
        s.nome = ''
        s.data_nasc = ''
        s.cel = ''
    

    def seApresentar(s): # comportamentos
        return f'Olá, meu nome é {s.nome}, e tenho {s.idade} anos.'

    def retornaAnoQueNasceu(s):
        return s.data_nasc

    def retornaSalarioComBonus(s, salario):
        return salario * 1

class Gerente(Pessoa):
    def __init__(self,
                 cpf='111111', 
                 nome='Teste',
                 data_nasc='99/99/9999',
                 idade=99):

        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc
        self.idade = idade
        self.bonus = 1.5
        
    def retornaSalarioComBonus(self, salario):
        return salario * self.bonus



