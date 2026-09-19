# =============================================================
# Exercício 6 — Detecção de anomalias em velocidades de veículos
# =============================================================
# Contexto: radar em uma via urbana.
# [velocidade (km/h), hora do dia]
# Velocidades normais: entre 52 e 66 km/h, ao longo do dia.
# Duas situações incomuns foram inseridas.
# =============================================================
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

velocidades = [
    [55, 8], [62, 8], [58, 9], [65, 10], [60, 12],
    [52, 14], [57, 15], [64, 16], [61, 17], [59, 18],
    [63, 19], [56, 20], [66, 21], [155, 3], [20, 8]
]

dados = np.array(velocidades)

# 2 situações incomuns em 15 observações
modelo = IsolationForest(n_estimators=100,
                         contamination=2 / len(dados),
                         random_state=42)

modelo.fit(dados)
rotulos = modelo.predict(dados)

print("=" * 58)
print("  Exercício 6 — Velocidades de veículos (radar)")
print("=" * 58)
print(f"  Observações       : {len(dados)}")
print(f"  Características   : 2 (velocidade km/h, hora)")
print("-" * 58)
print("  Velocidade | Hora | Classificação")
print("-" * 58)
for vel, hora, rotulo in zip(dados[:, 0], dados[:, 1], rotulos):
    classe = "normal" if rotulo == 1 else "CANDIDATO A OUTLIER"
    print(f"  {vel:>9} | {hora:>4} | {classe}")
print("-" * 58)

candidatos = dados[rotulos == -1]
print("  Candidatos (velocidade, hora) : "
      + str(candidatos.tolist()))
print("=" * 58)

# -------------------------------------------------------------
# Análise de cada candidato
# -------------------------------------------------------------
print(" Análise dos candidatos:")
print()
print("  1) [155 km/h às 3h]")
print("     Erro:     possível falha do radar (velocidade")
print("               improvável em via urbana).")
print("     Legítimo: racha/adrenalina a madrugada, veículo não")
print("               autorizado em alta velocidade.")
print("     Veredito: CASO PARA INVESTIGAÇÃO — verificar o")
print("               registro do radar antes de multar.")
print()
print("  2) [20 km/h às 8h]")
print("     Erro:     improvável a via toda a 20 km/h sem motivo.")
print("     Legítimo: horário de pico — congestionamento ou")
print("               acidente deixando o trânsito parado.")
print("     Veredito: EVENTO LEGÍTIMO (congestionamento), mas")
print("               merece verificação rápida: se for um")
print("               acidente, foi resolvido depois?")

# -------------------------------------------------------------
# Gráfico
# -------------------------------------------------------------
plt.figure(figsize=(7, 5))
normais = dados[rotulos == 1]
candidato = dados[rotulos == -1]

plt.scatter(normais[:, 1], normais[:, 0],
            color="#2d6cdf", s=80, label="Normal")
plt.scatter(candidato[:, 1], candidato[:, 0],
            color="#e74c3c", s=120, label="Candidato a outlier")

plt.xlabel("Hora do dia")
plt.ylabel("Velocidade (km/h)")
plt.title("Velocidades em via urbana — Isolation Forest")
plt.legend()
plt.grid(True)
plt.show()