Windows
  Requisitos
    Windows 10 ou superior atualizado
    WSL versão 1.1.3 ou superior
    
  WSL
    https://learn.microsoft.com/pt-br/windows/wsl/install
    1. No PowerShell como administrador.
    wsl --install
    2. Reiniciar e depois abrir a nova aplicação disponível “Ubuntu”. (Ubuntu é padrão)
    3. Vai pedir para criar um usuário e senha para o sistema Linux. Após definir, está pronto para uso.
    
  Docker Desktop
    1. Baixar instalador e instalar
    https://docs.docker.com/desktop/install/windows-install/
    2. Após reiniciar novamente, já pode testar
    docker run hello-world


Linux
  https://docs.docker.com/desktop/install/linux-install/
  Instalação Docker e docker-compose 2
  Pode usar o package da sua distribuição ou instalar com os passos abaixo
  1. Atualizar o sistema
  sudo apt update
  sudo apt upgrade
  2. Instalar pacotes necessários
  sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
  3. Adicionar repositório do docker
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release
  4. Instalar o docker
  sudo apt-get install docker-ce
  5. Verificar se deu certo
  sudo systemctl status docker
  6. Adicionar usuário ao grupo docker
  sudo usermod -aG docker ${USER}
  7. Só reiniciar e testar
  docker run hello-world


Após a instalação do docker crie uma pasta onde deseja guardar o projeto.
acesse a pasta via terminal
clone o repositorio:
  git clone https://github.com/MichelWars/Sistema-Gestao-Estoque.git
dentro da pasta do projeto execute
  docker-compose up
  para criar os containers e executar as aplicações.
nas proximas vezes execute com 
  docker-compose up --build
Garantar que o docker desktop esta sendo executado para que os comandos funcionem.
