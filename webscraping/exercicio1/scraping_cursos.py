import requests
from bs4 import BeautifulSoup

def main():
    url = "http://127.0.0.1:8000/exercicio1/index.html"
    
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

    cursos = soup.find_all("div", class_="curso")

    print(f"Total de cursos encontrados: {len(cursos)}\n" + "=" * 50)

    for i, curso in enumerate(cursos, start=1):
        nome = curso.find("h2", class_="nome").get_text(strip=True)
        area = curso.find("p", class_="area").get_text(strip=True).replace("Área:", "").strip()
        carga_horaria = curso.find("p", class_="carga-horaria").get_text(strip=True).replace("Carga Horária:", "").strip()
        
        assuntos_itens = curso.find("ul", class_="assuntos").find_all("li")
        assuntos = [item.get_text(strip=True) for item in assuntos_itens]

        print(f"Curso {i}: {nome}")
        print(f"  • Área: {area}")
        print(f"  • Carga Horária: {carga_horaria}")
        print("  • Assuntos Estudados:")
        for assunto in assuntos:
            print(f"      - {assunto}")
        print("-" * 50)

if __name__ == "__main__":
    main()

