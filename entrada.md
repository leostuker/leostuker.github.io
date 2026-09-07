sessao = rpg
titulo_sessao = RPG
descricao = Banco de dados das magias de D&D em portugues.

# Grimorio de D&D

Com o início da cadeira de Banco de Dados Geográficos, comecei a ler sobre bancos de dados e quis construir um banco para experimentar algumas coisas e me familiarizar com os conceitos. Simultaneamente, precisei separar as magias de bardo de terceiro círculo, o que foi uma tarefa bastante trabalhosa. Então, unindo o útil ao agradável, criei um banco de dados com todas as magias presentes no Livro do Jogador de 2024, pois havia um documento markdown fornecido pelo grupo [Heróis Anonimos](https://sites.google.com/view/heroisanonimos/ldj-2024), que traduziu o livro.

Instalei uma stack no meu servidor doméstico com PostgreSQL junto ao Adminer, que possibilita trabalhar no PostgreSQL tanto com uma interface quanto via comandos SQL. Como meu interesse era no backend, para poder utilizá-lo, criei com o Google AI Studio um frontend simples onde é possível adicionar, filtrar e exportar magias com facilidade. Estou mantendo o projeto disponível através do endereço [grimorio.leonardo.stuker.nom.br](https://grimorio.leonardo.stuker.nom.br/), hospedado no meu próprio servidor e disponibilizado via Cloudflare Tunnel.

[carousel]
url_01	descricao 01
url_02	descricao 02
url_03	descricao 03
url_04	descricao 04
url_05	descricao 05
[/carousel]