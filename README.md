## Iara Games API

Este repositório contém a API para o projeto Iara Games, desenvolvida usando Python e o framework FastAPI.
A  API fornece funcionalidades essenciais para a listagem de jogos na seção da loja do projeto Iara Games.

### Funcionalidades

- Listagem de jogos disponíveis na loja
- Integração com o banco de dados para recuperar informações dos jogos


## Configurar o Ambiente de Desenvolvimento do Back-End

1. Navegar para o diretório do back-end:
cd Iara-Games-API

2. Criar um ambiente virtual:
python -m venv venv

3. Ativar o ambiente virtual:
  - No Windows: 
  .\venv\Scripts\activate

  - No macOS/Linux
  source venv/bin/activate

4. Instalar as dependências:
pip install -r requirements.txt

5. Criar um arquivo .env com as configurações do seu banco de dados.

7. Executar a API:
fastapi dev

8. Isso iniciará a API no endereço http://127.0.0.1:8000.


