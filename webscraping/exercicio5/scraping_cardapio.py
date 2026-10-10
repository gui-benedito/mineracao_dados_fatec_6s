import requests
from bs4 import BeautifulSoup

def main():
    url = "http://127.0.0.1:8000/exercicio5/index.html"

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

    # Localizar cada seção do cardápio
    secoes = soup.find_all("section", class_="categoria-secao")

    print("=" * 65)
    print("CARDÁPIO DO RESTAURANTE ORGANIZADO POR CATEGORIAS")
    print("=" * 65)

    for secao in secoes:
        nome_categoria = secao.find("h2", class_="categoria-titulo").get_text(strip=True)
        print(f"\n📂 [{nome_categoria.upper()}]")
        print("-" * 65)

        # Percorrer apenas os itens pertencentes àquela seção
        itens = secao.find_all("article", class_="item")
        for item in itens:
            nome_item = item.find("h3", class_="nome").get_text(strip=True)
            descricao = item.find("p", class_="descricao").get_text(strip=True)
            preco = item.find("span", class_="preco").get_text(strip=True)

            print(f"  • {nome_item} - {preco}")
            print(f"    Descrição: {descricao}")
            print()

    print("=" * 65)

if __name__ == "__main__":
    main()

