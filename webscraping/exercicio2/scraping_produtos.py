import requests
from bs4 import BeautifulSoup

def main():
    url = "http://127.0.0.1:8000/exercicio2/index.html"

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

    elementos_produto = soup.find_all("div", class_="produto")
    produtos = []

    for elem in elementos_produto:
        nome = elem.find("h2", class_="nome").get_text(strip=True)
        fabricante = elem.find("p", class_="fabricante").get_text(strip=True).replace("Fabricante:", "").strip()
        categoria = elem.find("p", class_="categoria").get_text(strip=True).replace("Categoria:", "").strip()
        preco = elem.find("p", class_="preco").get_text(strip=True).replace("Preço:", "").strip()
        estoque = elem.find("span", class_="status").get_text(strip=True)

        produtos.append({
            "nome": nome,
            "fabricante": fabricante,
            "categoria": categoria,
            "preco": preco,
            "estoque": estoque
        })

    print("=" * 60)
    print("TODOS OS PRODUTOS ENCONTRADOS")
    print("=" * 60)
    for i, prod in enumerate(produtos, start=1):
        print(f"Produto {i}: {prod['nome']}")
        print(f"  • Fabricante: {prod['fabricante']}")
        print(f"  • Categoria : {prod['categoria']}")
        print(f"  • Preço     : {prod['preco']}")
        print(f"  • Situação  : {prod['estoque']}")
        print("-" * 60)

    produtos_disponiveis = [p for p in produtos if p["estoque"].lower() == "disponível"]

    print("\n" + "=" * 60)
    print("PRODUTOS DISPONÍVEIS EM ESTOQUE")
    print("=" * 60)
    for prod in produtos_disponiveis:
        print(f"• {prod['nome']} ({prod['fabricante']}) - {prod['preco']} [{prod['categoria']}]")
    print("=" * 60)

if __name__ == "__main__":
    main()

