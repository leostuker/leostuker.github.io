import markdown as markdown
import os
from datetime import datetime
from pathlib import Path
import json

def ler_dicionarios(nome_arquivo="dados.jsonl"):
    dicionarios = []
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha_limpa = linha.strip()
                if linha_limpa:
                    dic = json.loads(linha_limpa)
                    dicionarios.append(dic)
    except FileNotFoundError:
        print("Arquivo não encontrado")
        
    return dicionarios

def index(ultimos_artigos):

    dados_index = {
        "descricao": "",
        "titulo": "",
        "corpo": [],
        "a1": ultimos_artigos[3],
        "a2": ultimos_artigos[2],
        "a3": ultimos_artigos[1],
        "a4": ultimos_artigos[0]
    }

    with open('../index.md', 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        
    for linha in linhas:
        linha_limpa = linha.strip()        
        if not linha_limpa:
            continue
        if linha_limpa.startswith("descricao"):
            dados_index["descricao"] = linha_limpa.replace("descricao = ", "").strip()
        elif linha_limpa.startswith("# "):
            dados_index["titulo"] = linha_limpa.replace("#", "").strip()
        else:
            linha_html = markdown.markdown(linha_limpa)
            dados_index["corpo"].append(linha_html)
            
    texto_corpo = "\n\t\t\t\t\t".join(dados_index["corpo"])

    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<title>Leão Bordado</title>
		<link rel="icon" type="image/svg+xml" href="/favicon.svg">
		<link rel="icon" type="image/png" href="/favicon.png">
		<link rel="apple-touch-icon" href="/apple-touch-icon.png">
		<link rel="manifest" href="/manifest.json">
		<link rel="preload stylesheet" href="style.css" as="style">
		<link rel="preconnect stylesheet" href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@400;700&display=swap">
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta name="description" content="{dados_index["descricao"]}">
		<meta name="author" content="Leonardo Sander Stüker">
	</head>
	<body>
		<div id="header-placeholder"></div>
		<main id="main-content">
			<div class="hero-banner">
				<h2>Leão Bordado</h2>
			</div>
			<article >
				<h4>{dados_index["titulo"]}</h4>
				{texto_corpo}
			</article>
			<section class="posts_recentes">
				<h3>Posts Recentes</h3>
				<article id=a1>
					<h4><a href="posts-{dados_index["a1"]["sessao"]}/{dados_index["a1"]["titulo"].replace(" ", "_").lower() + ".html"}">{dados_index["a1"]["titulo"]}</a></h4>
					{markdown.markdown(dados_index["a1"]["sinopse"])}
					<a href="posts-{dados_index["a1"]["sessao"]}/{dados_index["a1"]["titulo"].replace(" ", "_").lower() + ".html"}" class="read-more">Ver Mais</a>
				</article>
				<article id=a2>
					<h4><a href="posts-{dados_index["a2"]["sessao"]}/{dados_index["a2"]["titulo"].replace(" ", "_").lower() + ".html"}">{dados_index["a2"]["titulo"]}</a></h4>
					{markdown.markdown(dados_index["a2"]["sinopse"])}
					<a href="posts-{dados_index["a2"]["sessao"]}/{dados_index["a2"]["titulo"].replace(" ", "_").lower() + ".html"}" class="read-more">Ver Mais</a>
				</article>
				<article id=a3>
					<h4><a href="posts-{dados_index["a3"]["sessao"]}/{dados_index["a3"]["titulo"].replace(" ", "_").lower() + ".html"}">{dados_index["a3"]["titulo"]}</a></h4>
					{markdown.markdown(dados_index["a3"]["sinopse"])}
					<a href="posts-{dados_index["a3"]["sessao"]}/{dados_index["a3"]["titulo"].replace(" ", "_").lower() + ".html"}" class="read-more">Ver Mais</a>
				</article>
				<article id=a4>
					<h4><a href="posts-{dados_index["a4"]["sessao"]}/{dados_index["a4"]["titulo"].replace(" ", "_").lower() + ".html"}">{dados_index["a4"]["titulo"]}</a></h4>
					{markdown.markdown(dados_index["a4"]["sinopse"])}
					<a href="posts-{dados_index["a4"]["sessao"]}/{dados_index["a4"]["titulo"].replace(" ", "_").lower() + ".html"}" class="read-more">Ver Mais</a>
				</article>
			</section>
		</main>
		<div id="footer-placeholder"></div>
		<script src="scripts.js"></script>
	</body>
</html>
'''

    with open("index.html", 'w', encoding='utf-8') as f:
        f.write(html)

    return             

dados = ler_dicionarios()

dados_ordenados = sorted(dados, key=lambda x: datetime.strptime(x["data"], "%d/%m/%Y"))

index(dados_ordenados[-4:])
