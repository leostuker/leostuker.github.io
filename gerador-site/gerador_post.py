import markdown as markdown
import os
from datetime import date
from pathlib import Path
import json

def gerar_post(entrada):
    with open(entrada, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        
    dados = {
        "secao": "",
        "titulo_secao": "",
        "descricao": "",
        "data": "",
        "titulo": "",
        "sinopse" : "",
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
                if chave == "secao":
                    dados["secao"] = valor
                elif chave == "titulo_secao":
                    dados["titulo_secao"] = valor
                elif chave == "descricao":
                    dados["descricao"] = valor
                elif chave == "data":
                    if valor == "":
                        dados["data"] = date.today().strftime("%d/%m/%Y")
                    else:
                        dados["data"] = valor
            elif linha_limpa.startswith("#"):
                dados["titulo"] = linha_limpa.replace("#", "").strip()
                fase = "sinopse"
                
        elif fase == "sinopse":
            if linha_limpa.startswith("#"):
                linha_html = markdown.markdown(linha_limpa)
                dados["corpo"].append(linha_html)
            else:
                dados["sinopse"] = linha_limpa
                linha_html = markdown.markdown(linha_limpa)
                dados["corpo"].append(linha_html)
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
                    desc = partes[1].strip().replace('"', '&quot;')
                    dados["carousel"].append(f'\t\t\t\t\t\t\t<img src="{url}" alt="{desc}" loading="lazy">')
    
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
    \t\t\t\t\t<button class="carousel-button prev" aria-label="Foto Anterior"> &#9664; </button>
    \t\t\t\t\t<button class="carousel-button next" aria-label="Próxima Foto"> &#9654; </button>
    \t\t\t\t</div>'''
    
    nome_arquivo = dados["titulo"].replace(" ", "_").lower() + ".html"
    
    if dados["secao"] != "":
        url_path = f"posts-{dados['secao']}/{nome_arquivo}"
        pasta_destino = "..\posts-" + dados["secao"]
        os.makedirs(pasta_destino, exist_ok=True)
        saida = os.path.join(pasta_destino, nome_arquivo)
    else:
        url_path = nome_arquivo
        saida = nome_arquivo
            
    # Lendo o template e fragmentos (header/footer)
    with open('../header.html', 'r', encoding='utf-8') as f:
        html_header = f.read()
    with open('../footer.html', 'r', encoding='utf-8') as f:
        html_footer = f.read()
    with open('templates/post.html', 'r', encoding='utf-8') as f:
        template = f.read()
        
    html = template.format(
        titulo=dados["titulo"],
        titulo_secao=dados["titulo_secao"],
        descricao=dados["descricao"],
        url_path=url_path,
        texto_corpo=texto_corpo,
        bloco_carousel=bloco_carousel,
        header=html_header,
        footer=html_footer
    )
            
    with open(saida, 'w', encoding='utf-8') as f:
        f.write(html)

    print(dados["secao"], "\t",nome_arquivo)
        
    return dados

def zerar_dados(nome_arquivo="dados.jsonl"):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        pass

def salvar_dados(dados, nome_arquivo="dados.jsonl"):
    with open(nome_arquivo, "a", encoding="utf-8") as f:
        linha = json.dumps(dados, ensure_ascii=False)
        f.write(linha + "\n")

print("\nPosts:\nSeção\t Post")

zerar_dados()

for arquivo in Path("../").glob('posts-*/**/*.md'):
    dados = gerar_post(arquivo)
    del dados['corpo'], dados['carousel']
    salvar_dados(dados)
