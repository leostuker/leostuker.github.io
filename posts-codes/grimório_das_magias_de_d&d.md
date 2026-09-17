secao = codes
titulo_secao = Computação
descricao = Postagem sobre meu banco de dados das magias de D&D em português.
data = 01/09/2026

# Grimório das magias de D&D

Com o início da cadeira de Banco de Dados Geográficos, comecei a ler sobre bancos de dados e quis construir um banco para experimentar algumas coisas e me familiarizar com os conceitos. Simultaneamente, precisei separar as magias de bardo de terceiro círculo, o que foi uma tarefa bastante trabalhosa. Então, unindo o útil ao agradável, pensei em criar um banco de dados com todas as magias presentes no Livro do Jogador de 2024, pois havia um documento markdown fornecido pelo grupo [Heróis Anônimos](https://sites.google.com/view/heroisanonimos/ldj-2024), que traduziu todo o livro para o português, incluindo as magias presentes nele.

Iniciei o projeto montando uma stack Docker contendo o PostgreSQL e o Adminer. Esse setup me permitiu criar o banco de dados com uma interface simples e funcional, mas também através de comandos SQL, facilitando o desenvolvimento das habilidades necessárias para a cadeira. Criei, assim, um pequeno banco de dados formado por 5 tabelas e alguns tipos ENUM personalizados.

A principal é a tabela de magias, que contém quase todas as características que uma magia pode ter, como nome, círculo e duração. Além dessas características comuns, há também algumas mais específicas, como se gera uma salvaguarda e, caso sim, qual o atributo. Além dela, há também uma tabela com os livros para poder diferenciar magias "iguais" de origens diferentes, uma tabela de classes, uma tabela relacional de quais classes conjuram quais magias e, por fim, uma tabela sobre quais tipos de dano elas causam.

Evitei criar tabelas que seriam estáticas mesmo com o crescimento do banco. Para isso, usei tipos ENUM, que ao todo são 5: **atributos** para as salvaguardas, **dados** para a quantidade de dano causado, **escolas** para as escolas de magia, **formas** para as formas das áreas de dano e **tipo_dano** para a tabela que os relaciona com as magias. Vendo em retrospecto, sinto que poderiam ser tabelas, o que seria mais simples, mas achei interessantes os tipos personalizados.

Com o banco criado, senti necessidade de criar uma interface para procurar e filtrar as magias de forma intuitiva. Para isso, criei um webapp simples com filtros. No backend, usei Python com FastAPI para gerar as APIs e psycopg2 para acessar o SQL. No frontend, usei bastante HTML, fugindo ao máximo do JS. No entanto, para deixar tudo como quis, o JS foi preciso. Assim como todas as vezes que precisei usá-lo até hoje, não tenho ideia de como funciona e agradeço ao Gemini por ter feito (um dia ainda preciso entender o funcionamento dele). Além disso, me deparei com o TailwindCSS, que me parece interessante, mas uma parte de mim ainda acha que criar todo o meu CSS como quero é mais legal.

Atualmente, hospedo o projeto no meu servidor doméstico, fornecendo acesso pelo [grimorio.leonardo.stuker.nom.br](https://grimorio.leonardo.stuker.nom.br), sendo intermediado pelo Cloudflare Tunnel. Não vejo necessidade de algum serviço mais robusto em nenhum cenário que não seja por pura experimentação.