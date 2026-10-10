# Exercícios de Web Scraping - Mineração de Dados

Este repositório contém a resolução dos exercícios práticos de Web Scraping utilizando **Python**, **Requests** e **BeautifulSoup**.

---

## Estrutura de Diretórios

```text
webscraping/
│
├── Exercicios_Webscraping.pdf   # Descrição original das atividades
├── requirements.txt             # Dependências do projeto
├── README.md                    # Instruções de configuração e execução
│
├── exercicio1/                  # Exercício 1 — Catálogo de cursos
│   ├── index.html               # Página HTML da escola com os cursos
│   └── scraping_cursos.py       # Script Python de extração
│
└── exercicio2/                  # Exercício 2 — Loja de informática
    ├── index.html               # Página HTML com o catálogo de produtos
    └── scraping_produtos.py     # Script Python de extração e filtragem
```

---

## Configuração do Ambiente (Recomendado)

É uma boa prática criar e ativar um ambiente virtual (`venv`) para isolar as dependências:

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

Com a `venv` ativada, instale os pacotes via [`requirements.txt`](requirements.txt):

```bash
pip install -r requirements.txt
```

---

## Como Executar

### Passo 1: Iniciar o Servidor HTTP Local

O script precisa que as páginas estejam sendo servidas localmente. No diretório `webscraping`, inicie o servidor:

```bash
python -m http.server --bind 127.0.0.1 8000
```

> **Atenção:** Deixe este terminal em execução para manter o servidor ativo (acessível em `http://127.0.0.1:8000/`).

---

### Passo 2: Executar os Scripts de Raspagem

Abra um **novo terminal** na pasta `webscraping`, ative a `venv` (caso esteja usando) e execute:

#### Exercício 1 — Catálogo de Cursos
Acessa a página local, extrai nome, área, carga horária e a lista de assuntos abordados de cada curso:
```bash
python exercicio1/scraping_cursos.py
```

#### Exercício 2 — Loja de Informática
Acessa a página local, extrai todos os produtos cadastrados com seus detalhes e exibe um relatório geral e uma listagem filtrada apenas com itens em situação **Disponível**:
```bash
python exercicio2/scraping_produtos.py
```
