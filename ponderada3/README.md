# Criação de interface mobile para integração com API REST

## Descrição

Essa sessão tem o intuito de criar uma interface mobile integrada a um backend, que apresenta funcionalidade de login autenticado e filtro de imagem, no caso, remoção de fundo. Para isso, foi utilizado Flutter para o aplicativo, FastAPI para o backend, NGINX para o gateway e Docker para a conteinerização da aplicação.

## Instruções para execução

Para executar o projeto, é necessário ter o docker e o docker-compose instalados no computador. Caso não tenha, siga as instruções disponíveis no site oficial do [Docker](https://docs.docker.com/get-docker/).

Após a instalação, na raiz do projeto, execute o seguinte comando para subir o backend:

```bash
docker compose up
```

Para fazer utilização do projeto, é necessário ter um emulador ou um dispositivo físico conectado ao computador.

Após cumprir esse requisito, execute o seguinte comando, no diretório `mobile`, para rodar a aplicação:

```bash
flutter run
```

## Demonstração

Para a demonstração, foi capturado um vídeo da execução do projeto. O vídeo está disponível no seguinte link:

https://github.com/Pablo-RLV/Inteli-M10-T2/assets/99209107/d56c828f-bede-4fc7-80e7-8a16b0035e58
