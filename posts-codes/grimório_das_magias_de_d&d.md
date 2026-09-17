secao = codes
titulo_secao = Computação
descricao = Postagem sobre meu banco de dados das magias de D&D em português.
data = 01/09/2026

# Grimório das magias de D&D

Com o início da cadeira de Banco de Dados Geográficos, comecei a ler sobre bancos de dados e quis construir um banco para experimentar algumas coisas e me familiarizar com os conceitos. Simultaneamente, precisei separar as magias de bardo de terceiro círculo, o que foi uma tarefa bastante trabalhosa. Então, unindo o útil ao agradável, e pensei em criar um banco de dados com todas as magias presentes no Livro do Jogador de 2024, pois havia um documento markdown fornecido pelo grupo [Heróis Anonimos](https://sites.google.com/view/heroisanonimos/ldj-2024), que traduziu o livro para português de todo o livro incluindo as magias que estão nele.

Iniciei o projeto montanto uma stack docker contendo o PostgreSQL e o Adminer, com esse setup me permitia criar o banco de dados com uma interface simples e funcional, mas tambem atraves de comandos SQL, facilitando o desenvolvimento das habilidades nescessarias para a cadeira.
Criei assim um pequeno banco de dados formada por 5 tabelas e alguns tipos ENUM personalizados.

A principal tabela é a tabela das magias onde tem quase todas as caracteristicas que uma maiga pode ter, como nome, circulo, duração... Alem dessas caracteristicas comuns tambem algumas mais especificas como se gera uma salvaguarda e caso sim qual o atributo. Alem dela tambem uma tabela com os livros para poder diferenciar magias "iguais" de origens diferentes, uma tabela de classes, uma tabela relacional de quais classes conjuram quais magias, e por fim uma tabela de quais tipos de dano causa. 

Evitei criar tabelas que seriam estaticas mesmo com o crescimento do banco, para isso usei tipos ENUM ao todo são 5: **atributos** para as salvaguardas, **dados** para a quantidade de dano causado, **escolas** para as escolas de magia, **formas** para as formas das areas de dano e **tipo_dano** para a tabela que os relacina com as magias. Vendo em retrospecto sinto que poderiam ser tabelas que seria mais simples, mas achei interessante os tipos personalizados.

Com o banco criado senti nescessidade de criar uma inteface para procurar e filtrar as magias de forma intuitiva, para isso criei um webapp simples com filtros. No backend usei Py com FastAPI, para gerar as APIs, e psycopg2, para acessar o SQL. No frontend usei bastante html fugindo ao maximo de js, no entanto para deixar tudo como quis foi preciso, assim como todas vezes que precisei usar até hoje js não tenho ideia de como funciona e agradeço ao Gemini por ter feito (um dia ainda preciso entender o funcionamento dele). Alem disso me daparei com tailwindCSS, que me parece interessante, mas uma parte de mim ainda acha que criar todo meu css como quero é mais legal.

Atualmente hospedo no meu servidor domestico fornecendo acesso pelo [grimorio.leonardo.stuker.nom.br](https://grimorio.leonardo.stuker.nom.br/) sendo intermediado pelo Claudflare Tunnel. Não vejo nescessidade em algum serviço mais robusto em nenhum cenario, que não por pura espermentação.