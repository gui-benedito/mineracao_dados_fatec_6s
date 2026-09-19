# =============================================================
# Exercício 7 — Sensores ambientais (arquivo CSV)
# =============================================================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

dados = pd.read_csv("sensores_ambientais.csv")

print("=" * 56)
print("  Exercício 7 — Sensores ambientais")
print("=" * 56)
print(" Primeiras linhas do arquivo:")
print("-" * 56)
print(dados.head())
print("-" * 56)

# Características do modelo
caracteristicas = dados[["temperatura", "umidade"]]

# 3 leituras suspeitas em 20 observações
modelo = IsolationForest(n_estimators=100,
                         contamination=3 / len(dados),
                         random_state=42)

rotulos = modelo.fit_predict(caracteristicas)

# Adiciona a coluna rótulo (1 = normal, -1 = candidata)
dados["rotulo"] = rotulos

print(" Classificação adicionada à coluna 'rotulo':")
print("-" * 56)
print(dados)
print("-" * 56)

candidatas = dados[dados["rotulo"] == -1]
print(" Leituras candidatas:")
print("-" * 56)
print(candidatas[["id_leitura", "data", "temperatura", "umidade"]])
print("=" * 56)

# -------------------------------------------------------------
# Explicação das combinações incomuns
# -------------------------------------------------------------
print(" Explicação das combinações temperatura/umidade:")
print("  Padrão normal: temperatura entre 20 e 24 °C com umidade")
print("  entre 47 e 61 %. As três candidatas fogem desse padrão:")
print()
print("  - L011 (38 °C, 18 %): muito quente e muito seco.")
print("    Sugere falta de calibração do sensor ou ambiente")
print("    próximo a fonte de calor/ar-condicionado.");
print("  - L017 (8 °C, 92 %): muito frio e muito úmido.")
print("    Sugere leitura de câmara fria ou defeito do sensor.");
print("  - L020 (35 °C, 25 %): quente e seco, sem relação com o")
print("    padrão das demais leituras — combinação incomum.")
print()
print("  As duas características juntas revelam o problema:")
print("  uma temperatura ou umidade isolada ainda seria próxima")
print("  do esperado, mas a COMBINAÇÃO das duas não ocorre nos")
print("  sensores normais.")

# -------------------------------------------------------------
# Gráfico de dispersão
# -------------------------------------------------------------
plt.figure(figsize=(7, 5))
normal = dados[dados["rotulo"] == 1]
cand = dados[dados["rotulo"] == -1]

plt.scatter(normal["temperatura"], normal["umidade"],
            color="#2d6cdf", s=80, label="Normal")
plt.scatter(cand["temperatura"], cand["umidade"],
            color="#e74c3c", s=120, label="Candidata a outlier")

for _, linha in cand.iterrows():
    plt.annotate(linha["id_leitura"],
                 (linha["temperatura"], linha["umidade"]),
                 textcoords="offset points", xytext=(8, 8))

plt.xlabel("Temperatura (°C)")
plt.ylabel("Umidade (%)")
plt.title("Sensores ambientais — Isolation Forest")
plt.legend()
plt.grid(True)
plt.show()