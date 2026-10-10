import requests
from bs4 import BeautifulSoup

def main():
    url = "http://127.0.0.1:8000/exercicio6/index.html"

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

    artigos_evento = soup.find_all("article", class_="evento")

    print("=" * 70)
    print("AGENDA COMPLETA DE EVENTOS")
    print("=" * 70)

    for i, art in enumerate(artigos_evento, start=1):
        nome = art.find("h2", class_="nome").get_text(strip=True)
        data = art.find("p", class_="data").get_text(strip=True).replace("Data:", "").strip()
        horario = art.find("p", class_="horario").get_text(strip=True).replace("Horário:", "").strip()
        local = art.find("p", class_="local").get_text(strip=True).replace("Local:", "").strip()

        # Extrair múltiplos palestrantes
        tags_palestrantes = art.find("div", class_="palestrantes").find_all("span", class_="palestrante")
        palestrantes = [p.get_text(strip=True) for p in tags_palestrantes]

        # Extrair texto e href do link de inscrição
        link_tag = art.find("a", class_="link-inscricao")
        texto_link = link_tag.get_text(strip=True) if link_tag else "Sem link"
        href_link = link_tag.get("href", "") if link_tag else ""

        tem_multiplos_palestrantes = len(palestrantes) > 1

        print(f"Evento {i}: {nome}")
        print(f"  • Data/Horário   : {data} às {horario}")
        print(f"  • Local          : {local}")
        print(f"  • Palestrantes ({len(palestrantes)}) : {', '.join(palestrantes)}")
        
        # Indicar claramente eventos com mais de um palestrante
        if tem_multiplos_palestrantes:
            print("  ★ [DESTAQUE] Evento possui múltiplos palestrantes!")

        print(f"  • Link Inscrição : {texto_link} -> {href_link}")
        print("-" * 70)

if __name__ == "__main__":
    main()

