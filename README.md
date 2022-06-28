

1. Executar o comando para baixar o projeto **git clone https://Suzanneloures@bitbucket.org/Suzanneloures/recomendacao_de_rotas.git** .
2. Instalar Miniconda 
    - Miniconda é um instalador pequeno e gratuito para conda. É uma pequena versão bootstrap do Anaconda que inclui o conda, Python, os pacotes dos quais eles dependem e um pequeno número de outros pacotes úteis, incluindo pip, zlib e alguns outros.
    - https://docs.conda.io/en/latest/miniconda.html

3. Dentro da pasta do projeto ( user/your_path/recomendacao_de_rotas )executar o comando:
    - $ pip install -r requirements.txt
    - Esse comando instalará as dependencias necessárias para rodar o projeto
4. Executar comando Flask
    - flask run
5. Para executar o modulo Recomendação por Usuário:
    - Gerar uma chave de utilização para utilização da API Google 
    - (https://developers.google.com/maps/documentation/directions/start)
    - Ativar Geocoding API e Directions API
    - Adicionar a KEY no projeto
6. Para executar o modulo Avaliação
    - Informar <> ID de Usuário, nome da rota >
    - ex: < 21, farol_dique > 
