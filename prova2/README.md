# API em FastAPI para CRUD de blog

## Descrição

Para essa atividade, foi criado um CRUD de um blog utilizando o framework FastAPI. Aleḿ disso, os logs de acesso foram registrados em um arquivo de log., por meio da biblioteca logging. Essa API então foi colocada em um gateway, o que permite a comunicação entre a API e o cliente. Com o intuito de facilitar a execução do projeto, foi utilizado o Docker, que permite a criação de containers para a execução de aplicações.

## Execução

Para executar o projeto, é necessário ter o Docker instalado. Após isso, basta executar o comando abaixo na pasta `build` do projeto:

```bash
docker compose up
```

Caso não desejado, é possível executar o projeto sem o Docker, basta criar um ambiente virtual, a partir do seguinte comando:

```bash
python3 -m venv venv
```

E então instalar as dependências do projeto:

```bash
pip install -r requirements.txt
```

Após isso, basta executar o arquivo `main.py`:

```bash
python main.py
```

## Rotas

As rotas disponíveis são:

### GET /blog

Retorna todos os posts do blog.

### GET /blog/{id}

Retorna o post com o id especificado.

### POST /blog

Cria um novo post no blog.

### PUT /blog/{id}

Atualiza o post com o id especificado.

### DELETE /blog/{id}

Deleta o post com o id especificado.

Para a visualização completa das rotas e testes, é possível acessar a documentação da API por meio do arquivo json do Insomnia, presente no arquivo `Insomnia.json`

## Logs

Para visualizar os logs, basta acessar o arquivo `app.log` na pasta `logs`. Somente serão registrados os logs com nível de `WARNING` ou superior.

## Acesso à API

Para acessar a API, basta acessar o endereço `http://localhost:3000/` no navegador. Esse será o endereço do gateway, que redirecionará para a API.

Caso deseje acessar diretamente a API, basta acessar o endereço `http://localhost:5000/`.
