# Instalação do mongodb em um sistema Debian

#1: download e importação da chave para o repositorio - necessário o gnupg instalado
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

#2: adicionar  endereço do repositório em um novo arquivo no sources.list.d/
echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

#3: atualizar a lista de repositórios do apt
sudo apt update

#4: instalar o mongo via apt
sudo apt-get install -y mongodb-org

#5: inicializar o serviço do mongodb
sudo systemctl start mongod

#6: verificar status do serviço
sudo systemctl status mongod
