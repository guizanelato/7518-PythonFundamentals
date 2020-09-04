
import unittest
import random
from app import *

class testeDanca(unittest.TestCase):
    
    def setUp(self):
        return DancaDasCadeiras()
    
    def setUpParticipantes(self, jogo):
        for num in range(random.randint(1,10)):
            jogo.adicionaParticipantes(num)

    def test_VerificaInicioDeDisputa(self):
        jogo = self.setUp()
        ### validação do funcionamento
        jogo.iniciarDisputa()
        self.assertEqual(True, jogo.ativo)

    def test_VerificaAdicaoDeParticipantes(self):
        jogo = self.setUp()
        jogo.adicionaParticipantes('player1')
        self.assertEqual(1,jogo.num_participantes)
        self.assertEqual('player1', jogo.participantes[0])

    def test_DefinicaoNumeroDeCadeiras(self):
        jogo = self.setUp()
        self.setUpParticipantes(jogo)
        jogo.definirNumeroDeCadeiras()
        self.assertEqual(jogo.num_participantes-1,jogo.num_cadeiras)



