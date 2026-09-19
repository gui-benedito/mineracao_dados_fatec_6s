# =============================================================
# Exercício 3 — Consumo de combustível
# =============================================================
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

consumo = [
    [10, 1.0], [20, 1.8], [30, 2.6],
    [40, 3.5], [50, 4.3], [60, 5.1],
    [70, 6.0], [80, 7.0], [90, 8.0],
    [100, 20.0]
]

dados = np.array(consumo)

# 1 candidato em 10 observações
modelo = IsolationForest(n_estimators=100,
                         contamination=1 / len(dados),
                         random_state=42)

modelo.fit(dados)
rotulos = modelo.predict(dados)

print("=" * 56)
print("  Exercício 3 — Consumo de combustível")
print("=" * 56)
print(f"  Observações       : {len(dados)}")
print(f"  Características   : 2 (distância km, litros)")
print("-" * 56)
print("  Distância | Litros | Classificação")
print("-" * 56)
for dist, litros, rotulo in zip(dados[:, 0], dados[:, 1], rotulos):
    classe = "normal" if rotulo == 1 else "CANDIDATO A OUTLIER"
    print(f"  {dist:>9} | {litros:>6} | {classe}")
print("-" * 56)

candidatos = dados[rotulos == -1]
print("  Combinação incomum (km, litros) : "
      + str(candidatos.tolist()))
print("=" * 56)

# -------------------------------------------------------------
# Explicação
# -------------------------------------------------------------
print(" Explicação — por que analisar distância e litros juntos:")
print("  Nas viagens normais, os litros crescem de forma")
print("  proporcional à distância (≈0,085 L/km): 60 km -> 5,1 L,")
print("  80 km -> 7,0 L. A combinação [100 km, 20,0 L] quebra")
print("  essa proporção (20 L/100 km = 0,20 L/km).")
print()
print("  Analisando cada característica sozinha, nem 100 km nem")
print("  20 L são absurdos individualmente — o ANÔMALO é a")
print("  relação entre elas. Por isso o Isolation Forest recebe")
print("  as duas características juntas: ele captura a combinação")
print("  incomum que uma análise unidimensional não veria.")

# -------------------------------------------------------------
# Gráfico de dispersão
# -------------------------------------------------------------
plt.figure(figsize=(7, 5))
normais = dados[rotulos == 1]
candidato = dados[rotulos == -1]

plt.scatter(normais[:, 0], normais[:, 1],
            color="#2d6cdf", s=80, label="Normal")
plt.scatter(candidato[:, 0], candidato[:, 1],
            color="#e74c3c", s=120, label="Candidato a outlier")

plt.xlabel("Distância (km)")
plt.ylabel("Litros consumidos (L)")
plt.title("Consumo de combustível — Isolation Forest")
plt.legend()
plt.grid(True)
plt.show()
