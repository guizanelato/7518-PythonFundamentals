
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs

#0: url de exemplo do projeto
url = 'https://www.al.sp.gov.br/propositura/?id=1000252923&tipo=1&ano=2018'

#1: Conseguir fazer o python se comunicar com o website da ALESP
with urlopen(url) as pagina:
    conteudo = pagina.read()

#2: Extrair o conteúdo do site
pagina_estruturada = bs(conteudo, 'html.parser') 

#3: Aplicar um filtro para recuperar dados de interesse

div_alvo = pagina_estruturada.findAll("div", {"class": "ativo", "id":"referencias"})

tabela = div_alvo[0].table.tbody.find_all('td')

#4: Armazenar os dados em uma estrutura fácil disponível no python

pl = {}

pl['num_legislativo'] = tabela[3].text.strip()[0:3] + '/' + tabela[3].text.strip()[-1:-5:-1]
pl['ementa'] = tabela[5].text.strip()
pl['data_publicacao'] = tabela[7].text.strip()
pl['regime'] = tabela[9].text.strip()
pl['autores'] = tabela[11].text.strip()
pl['apoiadores'] = tabela[13].text.strip()
pl['indexadores'] = tabela[15].text.strip()
pl['etapa_atual'] = tabela[17].text.strip() 


# gravar em um arquivo csv


