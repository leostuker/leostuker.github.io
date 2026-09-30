# Regras de Escrita para Postagens e Conteúdo do Site

Ao redigir postagens de blog ou conteúdo pessoal para o usuário neste repositório, o agente DEVE adotar estritamente o seguinte estilo de escrita:

1. **Tom e Ponto de Vista**: 
   - Escreva sempre em primeira pessoa ("eu", "meu", "fiz").
   - O tom deve ser conversacional, relaxado, prático, humilde, porém confiante (como alguém compartilhando uma história ou aprendizado de um projeto pessoal).
   - Não use jargão corporativo ou linguagem engessada.
   
2. **Narrativa e Estrutura**:
   - Misture detalhes técnicos com motivações pessoais e o contexto da situação ("Depois de anos tendo a ideia...", "Quando entrei na onda da auto-hospedagem...").
   - Foque na "jornada" e na história de desenvolvimento (tentativas, erros, frustrações e soluções finais).
   - Use cabeçalhos claros (`#`, `##`) para dividir seções e parágrafos curtos a médios.

3. **Vocabulário (PT-BR)**:
   - Use um Português do Brasil natural, com expressões coloquiais fluidas e cotidianas (ex: "garimpei", "xodó", "cadeira" ao se referir a disciplina de faculdade, "unindo o útil ao agradável").
   - Mantenha fluidez e conexão entre as ideias, usando frequentemente ações sequenciais ("Procurando por hosts gratuitos, encontrei...", "Isso me levou a pensar...").

4. **Frontmatter e Metadados**:
   - NÃO use o padrão YAML com `---`. O frontmatter deve ser estritamente no formato `chave = valor`.
   - **Para Posts (artigos e publicações)**, use EXATAMENTE as seguintes chaves e opções de valores permitidas:
     - `secao = [codes | fotos | rpg]` (Nota: a chave é sempre "secao", evite usar "sessao")
     - `titulo_secao = [Computação | Fotografias | RPG]` (De acordo com a seção escolhida acima)
     - `descricao = [texto livre com o resumo da postagem]`
     - `data = DD/MM/AAAA` (ou pode deixar vazio para assumir a data atual)
   - **Para Páginas Raiz (como index, sobre, etc)**, as chaves mapeadas são:
     - `titulo = [texto livre]`
     - `titulo_banner = [texto livre]`
     - `subtitulo = [texto livre]`
     - `descricao = [texto livre]`
   - **Carrosséis de Imagens**: Para postagens de fotos, os carrosséis devem ser adicionados no final do arquivo usando o formato:
     ```
     [carousel]
     url_da_imagem_01   descrição da imagem 01
     url_da_imagem_02   descrição da imagem 02
     [/carousel]
     ```
