import requests
from bs4 import BeautifulSoup

def main():
    url = "http://127.0.0.1:8000/exercicio4/index.html"

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

    elementos_livro = soup.find_all("div", class_="livro")
    livros = []

    print("=" * 65)
    print("TODOS OS LIVROS DA BIBLIOTECA")
    print("=" * 65)

    for i, elem in enumerate(elementos_livro, start=1):
        titulo = elem.find("h2", class_="titulo").get_text(strip=True)
        autor = elem.find("p", class_="autor").get_text(strip=True).replace("Autor:", "").strip()
        ano = elem.find("p", class_="ano").get_text(strip=True).replace("Ano:", "").strip()
        genero = elem.find("p", class_="genero").get_text(strip=True).replace("Gênero:", "").strip()
        situacao = elem.find("span", class_="status").get_text(strip=True)
        
        tags_kw = elem.find("div", class_="palavras-chave").find_all("li")
        palavras_chave = [kw.get_text(strip=True) for kw in tags_kw]

        livros.append({
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "genero": genero,
            "situacao": situacao,
            "palavras_chave": palavras_chave
        })

        print(f"Livro {i}: {titulo}")
        print(f"  • Autor     : {autor}")
        print(f"  • Ano       : {ano}")
        print(f"  • Gênero    : {genero}")
        print(f"  • Situação  : {situacao}")
        print(f"  • Tags      : {', '.join(palavras_chave)}")
        print("-" * 65)

    # Filtrar apenas livros que estejam Disponíveis
    livros_disponiveis = [l for l in livros if l["situacao"].lower() == "disponível"]

    print("\n" + "=" * 65)
    print("LIVROS DISPONÍVEIS PARA EMPRÉSTIMO")
    print("=" * 65)
    for livro in livros_disponiveis:
        print(f"📖 {livro['titulo']} ({livro['ano']})")
        print(f"   Autor: {livro['autor']} | Gênero: {livro['genero']}")
        print(f"   Palavras-chave: {', '.join(livro['palavras_chave'])}")
        print("-" * 65)

if __name__ == "__main__":
    main()

