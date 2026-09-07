import markdown as markdown
import os

with open("entrada.md", 'r', encoding='utf-8') as f:
    linhas = f.readlines()

dados = {
    "sessao": "",
    "titulo_sessao": "",
    "descricao": "",
    "titulo": "",
    "corpo": [],
    "carousel": []
}

fase = "cabecalho"

for linha in linhas:
    linha_limpa = linha.strip()
        
    if not linha_limpa:
        continue

    if fase == "cabecalho":
        if "=" in linha_limpa:
            chave, valor = linha_limpa.split("=", 1)
            chave = chave.strip()
            valor = valor.strip()
            if chave == "sessao":
                dados["sessao"] = valor
            elif chave == "titulo_sessao":
                dados["titulo_sessao"] = valor
            elif chave == "descricao":
                dados["descricao"] = valor
        elif linha_limpa.startswith("#"):
            dados["titulo"] = linha_limpa.replace("#", "").strip()
            fase = "corpo"

    elif fase == "corpo":
        if linha_limpa == "[carousel]":
            fase = "carousel"
        else:
            linha_html = markdown.markdown(linha_limpa)
            dados["corpo"].append(linha_html)
            
    elif fase == "carousel":
        if linha_limpa == "[/carousel]":
            fase = "fim"
        else:
            partes = linha_limpa.split("\t")
            if len(partes) >= 2:
                url = partes[0].strip()
                desc = partes[1].strip()
                dados["carousel"].append(f'\t\t\t\t\t\t\t<img src="{url}" alt="{desc}">')

texto_corpo = "\n\t\t\t\t".join(dados["corpo"])
	
bloco_carousel = ""
if dados["carousel"]:
    texto_imgs = "\n".join(dados["carousel"])
    bloco_carousel = f'''
\t\t\t\t<div class="carousel-container">
\t\t\t\t\t<div class="carousel-viewport">
\t\t\t\t\t\t<div class="carousel-slides">
{texto_imgs}
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
\t\t\t\t\t<button class="carousel-button prev"> &#9664 </button>
\t\t\t\t\t<button class="carousel-button next"> &#9654 </button>
\t\t\t\t\t<div class="carousel-dots"></div>
\t\t\t\t</div>'''

html = f'''<!DOCTYPE html>
<html lang="pt-BR">
\t<head>
\t\t<title>Leão Bordado - {dados["titulo_sessao"]}</title>
\t\t<link rel="icon" type="image/svg+xml" href="/favicon.svg">
\t\t<link rel="icon" type="image/png" href="/favicon.png">
\t\t<link rel="apple-touch-icon" href="/apple-touch-icon.png">
\t\t<link rel="manifest" href="/manifest.json">\t\t<link rel="stylesheet" href="../style.css">
\t\t<link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@400;700&display=swap" rel="stylesheet">
\t\t<meta charset="UTF-8">
\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">
\t\t<meta name="description" content="{dados["descricao"]}">
\t\t<meta name="author" content="Leonardo Sander Stüker">
\t</head>
\t<body>
\t\t<div id="header-placeholder"></div>
\t\t<main>
\t\t\t<div class="hero-banner">
\t\t\t\t<h2>{dados["titulo_sessao"]}</h2>
\t\t\t</div>
\t\t\t<main id="main-content">
\t\t\t<article>{dados["titulo"]}</h4>
\t\t\t\t{texto_corpo}{bloco_carousel}
\t\t\t</article>
\t\t</main>
\t\t<div id="footer-placeholder"></div>
\t\t<script src="../scripts.js"></script>
\t</body>
</html>'''

nome_arquivo = dados["titulo"].replace(" ", "_") + ".html"
if dados["sessao"] != "":
    pasta_destino = "posts-" + dados["sessao"]
    os.makedirs(pasta_destino, exist_ok=True)
    saida = os.path.join(pasta_destino, nome_arquivo)
else:
    saida = nome_arquivo
with open(saida, 'w', encoding='utf-8') as f:
    f.write(html)








