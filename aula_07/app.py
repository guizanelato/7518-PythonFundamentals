
import random
import time

class DancaDasCadeiras:
    def __init__(self):
        self.num_cadeiras = 0
        self.participantes = []
        self.num_participantes = 0
        self.ativo = False
    
    def iniciarDisputa(self):
        self.ativo = True

    def definirNumeroDeCadeiras(self):
        self.num_cadeiras = self.num_participantes - 1 

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
    
    def adicionaParticipantes(self, nome_jogador):
        self.participantes.append(nome_jogador)
        self.num_participantes += 1
    
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
