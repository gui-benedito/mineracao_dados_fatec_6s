import requests
from bs4 import BeautifulSoup

def main():
    url = "http://127.0.0.1:8000/exercicio3/index.html"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        print("Certifique-se de que o servidor HTTP local está em execução na pasta 'webscraping':")
        print("python -m http.server --bind 127.0.0.1 8000")
        return

    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")

    artigos = soup.find_all("article", class_="noticia")
    noticias = []

    print("=" * 70)
    print("TODAS AS NOTÍCIAS EXTRAÍDAS")
    print("=" * 70)

    for i, art in enumerate(artigos, start=1):
        categoria = art.find("span", class_="categoria").get_text(strip=True)
        titulo = art.find("h2", class_="titulo").get_text(strip=True)
        data = art.find("time", class_="data").get_text(strip=True)
        autor = art.find("p", class_="autor").get_text(strip=True).replace("Por", "").strip()
        resumo = art.find("p", class_="resumo").get_text(strip=True)

        noticias.append({
            "categoria": categoria,
            "titulo": titulo,
            "data": data,
            "autor": autor,
            "resumo": resumo
        })

        print(f"[{categoria.upper()}] - {data}")
        print(f"Título : {titulo}")
        print(f"Autor  : {autor}")
        print(f"Resumo : {resumo}")
        print("-" * 70)

    # Filtrar títulos por categoria escolhida (ex: Tecnologia)
    categoria_alvo = "Tecnologia"
    titulos_filtrados = [
        n["titulo"] for n in noticias if n["categoria"].lower() == categoria_alvo.lower()
    ]

    print("\n" + "=" * 70)
    print(f"NOTÍCIAS DA CATEGORIA '{categoria_alvo.upper()}':")
    print("=" * 70)
    for titulo in titulos_filtrados:
        print(f"• {titulo}")
    print("=" * 70)

if __name__ == "__main__":
    main()

