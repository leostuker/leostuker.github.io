import markdown as markdown
import os

def gerar_pagina_auxiliar(nome_arquivo, com_canonical=False):
    caminho_md = f'../{nome_arquivo}.md'
    
    if not os.path.exists(caminho_md):
        print(f"Arquivo não encontrado: {caminho_md}")
        return
        
    dados_pag = {
        "descricao": "",
        "titulo": "",
        "titulo_banner": "",
        "corpo": []
    }
    
    with open(caminho_md, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        
    for linha in linhas:
        linha_limpa = linha.strip()        
        if not linha_limpa:
            continue
        if linha_limpa.startswith("descricao ="):
            dados_pag["descricao"] = linha_limpa.replace("descricao = ", "").strip()
        elif linha_limpa.startswith("titulo ="):
            dados_pag["titulo"] = linha_limpa.replace("titulo = ", "").strip()
        elif linha_limpa.startswith("titulo_banner ="):
            dados_pag["titulo_banner"] = linha_limpa.replace("titulo_banner = ", "").strip()
        else:
            linha_html = markdown.markdown(linha_limpa)
            dados_pag["corpo"].append(linha_html)
            
    texto_corpo = "\t\t\t\t" + "\n\t\t\t\t".join(dados_pag["corpo"])
    
    with open('../header.html', 'r', encoding='utf-8') as f:
        html_header = f.read().rstrip('\n')
    with open('../footer.html', 'r', encoding='utf-8') as f:
        html_footer = f.read().rstrip('\n')
    with open('templates/auxiliar.html', 'r', encoding='utf-8') as f:
        template = f.read()

    if com_canonical:
        canonical_tag = f'\t\t<link rel="canonical" href="https://leonardo.stuker.nom.br/{nome_arquivo}.html">\n'
    else:
        canonical_tag = ""

    html = template.format(
        titulo=dados_pag["titulo"],
        titulo_banner=dados_pag["titulo_banner"],
        descricao=dados_pag["descricao"],
        texto_corpo=texto_corpo,
        header=html_header,
        footer=html_footer,
        canonical_tag=canonical_tag
    )
    
    with open(f"../{nome_arquivo}.html", 'w', encoding='utf-8') as f:
        f.write(html)
    print(nome_arquivo + ".html")

print("\nPáginas Auxiliares:")
gerar_pagina_auxiliar("sobre", com_canonical=True)
gerar_pagina_auxiliar("404", com_canonical=False)
