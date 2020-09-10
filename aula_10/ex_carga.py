## generators 
### exemplo de aplicação de generators - carga de 100000 de registros no mongo
import resource
import time

from datetime import datetime
from random import randint 
from pymongo import MongoClient


# nomes aleatórios
nomes = ['Julio', 'Hector', 'Yago', 'Bryan', 'William', 'Ricardo', 'Rauny', 'Renato', 'Jorge', 'Rafael', 'Guilherme']

# generators de documentos
def gerarDic(quantidade): 
	for documento in range(0,quantidade): 
		doc = {}
		doc['id']="{}{}{}".format(randint(10,99),randint(100,999),randint(1000,9999))
		doc['nome']=nomes[randint(0,len(nomes)-1)]
		doc['idade']= randint(20,35)
		doc['timestamp'] = str(datetime.now(tz=None))
		yield doc 
		
# conexão com o banco
con = MongoClient()

# cria banco+collection
collection = con.banco_dados.cadastro

# ingestão contanto o tempo
antes = time.clock()

teste = gerarDic(1000000)
for item in teste:
	collection.insert_one(item)
depois = time.clock()


#resultados
print("Memória utilizada: {}".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
print("Tempo de execução: {}".format(depois - antes))

        
        

