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
        "a1": ultimos_artigos[0],
        "a2": ultimos_artigos[1],
        "a3": ultimos_artigos[2],
        "a4": ultimos_artigos[3]
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

    posts = []
    for posicao in range(1, 5):
        artigo = dados_index[f"a{posicao}"]
        post = f'''				<article id="a{posicao}">
					<h4><a href="/posts-{artigo["secao"]}/{artigo["titulo"].replace(" ", "_").lower() + ".html"}">{artigo["titulo"]}</a></h4>
					{markdown.markdown(artigo["sinopse"])}
					<a href="/posts-{artigo["secao"]}/{artigo["titulo"].replace(" ", "_").lower() + ".html"}" class="read-more" aria-label="Ver Mais sobre {artigo["titulo"]}">Ver Mais</a>
				</article>'''
        posts.append(post)

    texto_posts = "\n".join(posts)

    with open('../header.html', 'r', encoding='utf-8') as f:
        html_header = f.read()
    with open('../footer.html', 'r', encoding='utf-8') as f:
        html_footer = f.read()
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        template = f.read()

    html = template.format(
        descricao=dados_index["descricao"],
        titulo=dados_index["titulo"],
        texto_corpo=texto_corpo,
        texto_posts=texto_posts,
        header=html_header,
        footer=html_footer
    )

    with open("../index.html", 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html")

    return             

def gerar_pag_post(artigos, secao):

    dados_pag = {
        "descricao": "",
        "titulo": "",
        "subtitulo": "",
        "corpo": []
    }

    dados_pag["titulo"] = artigos[0]["titulo_secao"]

    with open(f'../{secao}.md', 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        
    for linha in linhas:
        linha_limpa = linha.strip()        
        if not linha_limpa:
            continue
        if linha_limpa.startswith("descricao"):
            dados_pag["descricao"] = linha_limpa.replace("descricao = ", "").strip()
        elif linha_limpa.startswith("subtitulo"):
            dados_pag["subtitulo"] = linha_limpa.replace("subtitulo = ", "").strip()
        else:
            linha_html = markdown.markdown(linha_limpa)
            dados_pag["corpo"].append(linha_html)
            
    texto_corpo = "\n\t\t\t\t\t".join(dados_pag["corpo"])
   
    posts = []
    
    for posicao, artigo in enumerate(artigos, 1):
        post = f'''				<article id="a{posicao}">
					<h4><a href="/posts-{artigo["secao"]}/{artigo["titulo"].replace(" ", "_").lower() + ".html"}">{artigo["titulo"]}</a></h4>
					{markdown.markdown(artigo["sinopse"])}
					<a href="/posts-{artigo["secao"]}/{artigo["titulo"].replace(" ", "_").lower() + ".html"}" class="read-more" aria-label="Ver Mais sobre {artigo["titulo"]}">Ver Mais</a>
				</article>'''
        posts.append(post)

    texto_posts = "\n".join(posts)

    with open('../header.html', 'r', encoding='utf-8') as f:
        html_header = f.read()
    with open('../footer.html', 'r', encoding='utf-8') as f:
        html_footer = f.read()
    with open('templates/secao.html', 'r', encoding='utf-8') as f:
        template = f.read()

    html = template.format(
        titulo=dados_pag["titulo"],
        subtitulo=dados_pag["subtitulo"],
        descricao=dados_pag["descricao"],
        url_path=f"{secao}.html",
        texto_corpo=texto_corpo,
        texto_posts=texto_posts,
        header=html_header,
        footer=html_footer
    )

    with open(f"../{secao}.html", 'w', encoding='utf-8') as f:
        f.write(html)
    print(secao + ".html")
        
    return

dados = ler_dicionarios()

dados_ordenados = sorted(dados, key=lambda x: datetime.strptime(x["data"], "%d/%m/%Y"), reverse=True)

print("\nPaginas:")

index(dados_ordenados[:4])

posts_por_secao = {}

for item in dados_ordenados:
    secao = item["secao"]
    
    if secao not in posts_por_secao:
        posts_por_secao[secao] = []

    posts_por_secao[secao].append(item)

secoes = sorted(posts_por_secao.keys())

for secao in secoes:
    gerar_pag_post(posts_por_secao[secao], secao)
