# CriptoBank

### Descrição
Api para o cadastro de usuários e carteiras de ativos.

## Instalação
Este projeto utiliza como banco de dados o MySQL. Você deve inicialmente instala-lo em sua máquina e criar no mesmo um schema chamado:
> criptobank

Após clonar o projeto em sua pasta de preferencia, vá até o terminal, na pasta onde você fez a clonagem do projeto e executar o comando:
> pip install requirements.txt

Para configurar as informações do banco, vá até o arquivo /CriptoBank/settings.py, e altere as informações de HOST, NAME, USER e PASSWORD. Essas informações se encontra a partir da linha 78.

Em seguida, execute o comando:
> python manage.py migrate

Após isso, para iniciar a API, basta usar o seguinte comando ainda no terminal:
> python manage.py runserver

## Funcionalidades

### Cadastrar Usuário
Para cadastrar um usuário, você deve executar a seguinte URL em uma plataforma de API de sua preferencia:
```
Via POST:
127.0.0.1:8000/cadastra_usuario/
Passando como parametros via body:
nomeUsuario: Nome do Usuario
emailUsuario: Email do Usuario
```

### Criar Carteira
Para criar uma carteira:
```
Via POST:
127.0.0.1:8000/cadastra_carteira/
Passando como parametros via body:
nomeUsuario: Nome do Usuario
```

### Consultar Usuário
Para consultar um usuário:
```
Via GET:
127.0.0.1:8000/consulta_usuario/
Passando um dos seguintes parametros:
nomeUsuario: Nome do Usuario
emailUsuario: Email do Usuario
```

### Consultar Carteira
Para consultar uma carteira:
```
Via GET:
127.0.0.1:8000/consulta_carteira/
Passando o seguinte parametro:
idCarteira: ID da Carteira desejada
```

### Registrar Ativo
Para registrar ativos em uma carteira:
```
Via POST:
127.0.0.1:8000/registra_ativo/
Passando os seguintes parametros:
idCarteira: ID da Carteira
cripto: Nome do ativo a ser registrado
valor: Valor do ativo a ser registrado
```