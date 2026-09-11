# Exercícios Z-Score — Python

Série de 10 exercícios práticos sobre Z-Score para a disciplina de
Mineração de Dados (6º Semestre — FATEC).

## Exercícios

| Arquivo | Conceito |
|---------|----------|
| `exercicio_01.py` | Distância em passos de desvio-padrão |
| `exercicio_02.py` | Sinal do Z-Score (acima / abaixo / na média) |
| `exercicio_03.py` | Valor mais incomum e empate de \|Z\| |
| `exercicio_04.py` | Latência de API — outlier que infla o DP |
| `exercicio_05.py` | Monitoramento de CPU com classificação |
| `exercicio_06.py` | Mesmo valor em dois contextos distintos |
| `exercicio_07.py` | Função de classificação por Z-Score |
| `exercicio_08.py` | Z-Score em DataFrame com Pandas |
| `exercicio_09.py` | Comparação entre IQR e Z-Score |
| `exercicio_10.py` | Mini análise de eventos de segurança |

## Dependências

- Python 3.10+
- numpy
- pandas

## Como executar com ambiente virtual (venv)

### 1. Criar o ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar um exercício

```bash
python exercicio_01.py
```

### 5. Desativar o ambiente ao terminar

```bash
deactivate
```

---

## Orientações gerais

- Os exercícios 1, 2, 3, 6 e 7 usam **apenas Python puro** (sem bibliotecas externas).
- Os exercícios 4, 5 e 9 usam **NumPy**.
- Os exercícios 8 e 10 usam **NumPy + Pandas**.
