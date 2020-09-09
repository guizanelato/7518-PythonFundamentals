# Instalando mysql

#1: atualizar o repositório 
sudo apt update 

#2: caso não estiver instalado, instalar o gnupg
sudo apt install gnupg

#3: instalar o wget
sudo apt install wget

#4: instalar dependencia lsb-release
sudo apt install lsb-release

#4: realizar o download da configuração do repositório do mysql
wget https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb

#4.1: Selecionar OK (3 linha)

#5: atualizar a lista de repositórios do apt pós inserção do repo.mysql
sudo apt update

#6: instalar o mysql-server
sudo apt install mysql-server

# 6.1: aceitar as opções recomendadas

#7: verificar se o serviço está de pé e funcionando
sudo systemctl status mysql

#7.1: caso estiver em distros baseadas em Red Hat
sudo systemctl start mysqld && sudo systemctl enable 

#7.2 teste de acesso com usuário root
mysql -u root -p 

