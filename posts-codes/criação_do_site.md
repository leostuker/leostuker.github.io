secao = codes
titulo_secao = Computação
descricao = Postagem sobre a construção do meu site em suas varia fases.
data = 07/09/2026

# Criação do Site

## Primeira Fase

Depois de anos tendo a ideia de criar um site para usar como repositório de todas as minhas ideias e projetos, iniciei-o em 2025. Primeiro, pensei em usar o Google Sites para isso, mas ele não permitia que eu o deixasse da maneira que queria. Passei então para o WordPress, mas também me travava em algumas questões e praticamente tudo que eu queria eram funções pagas.

Mesmo assim, continuei a construção nele, já pensando em migrar para outro lugar depois ou até pagar a assinatura. Comprei meu domínio próprio pelo Registro.br e, quando fui colocá-lo no WordPress, ele negou, pois eu não havia comprado por eles e me cobrariam uma taxa para usar.

Foi então que decidi que construiria um site do zero. Procurando por hosts gratuitos, encontrei o GitHub Pages, que supria minhas necessidades. Com a ajuda de IA, fui criando e adicionando os elementos que queria. Configurei o DNS pela Cloudflare para conseguir o HTTPS no GitHub.

Como parte fundamental do site é mostrar minhas fotos, e são muitas fotos, não conseguiria usar apenas o 1GB de armazenamento que o GitHub oferece. Indo atrás de soluções, encontrei a Cloudinary, que me atende perfeitamente e duvido que terei problemas nos próximos anos.

## Segunda Fase

Quando entrei na onda da auto-hospedagem, pensei em hospedar meu site aqui mesmo, o que me levou a pensar em colocar mais conteúdo aqui. Isso me fez ir atrás de ferramentas para fazer isso de forma mais automática do que criar manualmente cada página e adicioná-la nas páginas adequadas, encontrando assim os geradores de sites estáticos (SSG).

A primeira ferramenta que testei foi o Hugo. Cheguei a gerar algumas páginas com ele, mas mesmo gastando muito tempo não conseguia colocar como eu queria. E menos ainda conseguia manter esse layout (questionável, mas meu) nas páginas. Testei mais uma pilha de alternativas, mas em nenhuma perdi muito tempo por já perceber que não seria possível fazer o que queria da forma que eu queria, muito menos entendendo o que estava acontecendo.

Essa frustração me levou à única alternativa possível: criar o meu próprio SSG. Durante os testes que fiz, entendi por cima a lógica de como eles funcionavam e parti disso. Sabia o que eu queria sempre manter e o que precisaria ser alterado em cada página. Assim, defini duas categorias de páginas a serem geradas: posts e páginas, sendo os posts, de fato, as postagens e as páginas, nada mais que um agregado de postagens. Como base, vários usavam documentos escritos em markdown, o que pensei ser um bom ponto de partida por já estar familiarizado graças ao Homebrewery.

Assim, defini o padrão de arquivo para ser a base dos posts: um arquivo .md, porém com algumas informações gerais no início, como seção, descrição e data do post. Com esse padrão, fiz um programa em Python para quebrar esse .md entre o antes e a partir do título. A primeira parte é referente a informações da página, que via de regra vão para o head, e o post em si, que vai para a main. Uma parte muito importante foi a presença das informações dos carrosséis de fotos, afinal, foi o que fez tudo isso iniciar. Na sequência, criei o padrão de markdown das páginas, que é bem mais simples, por contar apenas com informações básicas e uma breve descrição do que se trata.

