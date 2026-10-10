# Exercícios de Web Scraping - Mineração de Dados

Este repositório contém a resolução dos exercícios práticos de Web Scraping utilizando **Python**, **Requests** e **BeautifulSoup**.

---

## 📁 Estrutura de Diretórios

```text
webscraping/
│
├── Exercicios_Webscraping.pdf   # Descrição original das atividades
├── requirements.txt             # Dependências do projeto (requests, beautifulsoup4)
├── README.md                    # Instruções de configuração e execução
│
├── exercicio1/                  # Exercício 1 — Catálogo de cursos
│   ├── index.html               # Página HTML da escola com cursos e lista de assuntos
│   └── scraping_cursos.py       # Script de extração e exibição formatada
│
├── exercicio2/                  # Exercício 2 — Loja de informática
│   ├── index.html               # Catálogo com produtos e situações de estoque
│   └── scraping_produtos.py     # Script com extração geral e filtro por itens disponíveis
│
├── exercicio3/                  # Exercício 3 — Portal de notícias
│   ├── index.html               # Portal com notícias de diferentes categorias
│   └── scraping_noticias.py     # Script com extração geral e filtro de títulos por categoria
│
├── exercicio4/                  # Exercício 4 — Biblioteca
│   ├── index.html               # Acervo com livros, tags de palavras-chave e status
│   └── scraping_biblioteca.py   # Script de extração com exibição dos livros disponíveis
│
├── exercicio5/                  # Exercício 5 — Cardápio por categorias
│   ├── index.html               # Cardápio com seções: Pratos, Bebidas e Sobremesas
│   └── scraping_cardapio.py     # Script com navegação hierárquica por seção
│
└── exercicio6/                  # Exercício 6 — Agenda de eventos
    ├── index.html               # Agenda com eventos, links e múltiplos palestrantes
    └── scraping_eventos.py      # Script que extrai links e destaca múltiplos palestrantes
```

---

## ⚙️ Configuração do Ambiente (Recomendado)

Recomenda-se utilizar um ambiente virtual (`venv`) para isolar as dependências:

### 1. Criar o Ambiente Virtual

No terminal, dentro da pasta `webscraping`:

```bash
python -m venv venv
```

### 2. Ativar o Ambiente Virtual

* **No Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
  *(Se houver restrição de execução de scripts no PowerShell, execute antes: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`)*

* **No Windows (Prompt de Comando / CMD):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```

* **No Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar as Dependências

Com a `venv` ativada, instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como Executar

### Passo 1: Iniciar o Servidor HTTP Local

As páginas HTML devem ser servidas por um servidor HTTP local. No diretório `webscraping`, inicie o servidor:

```bash
python -m http.server --bind 127.0.0.1 8000
```

> **Atenção:** Mantenha esse terminal aberto para que os arquivos fiquem acessíveis em `http://127.0.0.1:8000/`.

---

### Passo 2: Executar os Scripts de Raspagem

Abra um **segundo terminal** no diretório `webscraping`, ative a `venv` (caso esteja usando) e execute o script desejado:

#### Exercício 1 — Catálogo de Cursos
Extrai nome, área, carga horária e a lista de 3 assuntos estudados por curso:
```bash
python exercicio1/scraping_cursos.py
```

#### Exercício 2 — Loja de Informática
Extrai os produtos e exibe um relatório geral e uma listagem filtrada de itens com estoque **Disponível**:
```bash
python exercicio2/scraping_produtos.py
```

#### Exercício 3 — Portal de Notícias
Extrai categoria, título, data, resumo e autor de todas as notícias, exibindo ao final os títulos de uma categoria específica (ex: Tecnologia):
```bash
python exercicio3/scraping_noticias.py
```

#### Exercício 4 — Biblioteca
Extrai detalhes dos livros (incluindo palavras-chave) e exibe separadamente os livros que estão **Disponíveis**:
```bash
python exercicio4/scraping_biblioteca.py
```

#### Exercício 5 — Cardápio por Categorias
Localiza cada seção do cardápio (*Pratos*, *Bebidas*, *Sobremesas*) e percorre os itens subordinados, preservando a hierarquia na saída:
```bash
python exercicio5/scraping_cardapio.py
```

#### Exercício 6 — Agenda de Eventos
Extrai eventos, texto e `href` dos links de inscrição, e sinaliza de forma destacada os eventos que possuem mais de um palestrante:
```bash
python exercicio6/scraping_eventos.py
```
