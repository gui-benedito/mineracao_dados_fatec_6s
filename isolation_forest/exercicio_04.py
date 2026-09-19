# =============================================================
# Exercício 4 — Viagens de ônibus urbano
# =============================================================
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

viagens = [
    [32, 3], [45, 5], [50, 4],
    [60, 6], [55, 5], [70, 7],
    [65, 6], [80, 8], [75, 7],
    [10, 45]
]

dados = np.array(viagens)

# 1 candidato em 10 observações
modelo = IsolationForest(n_estimators=100,
                         contamination=1 / len(dados),
                         random_state=42)

modelo.fit(dados)
rotulos = modelo.predict(dados)

print("=" * 56)
print("  Exercício 4 — Viagens de ônibus urbano")
print("=" * 56)
print(f"  Observações       : {len(dados)}")
print(f"  Características   : 2 (passageiros, atraso em min)")
print("-" * 56)
print("  Passageiros | Atraso | Classificação")
print("-" * 56)
for passag, atraso, rotulo in zip(dados[:, 0], dados[:, 1], rotulos):
    classe = "normal" if rotulo == 1 else "CANDIDATO A OUTLIER"
    print(f"  {passag:>10} | {atraso:>6} | {classe}")
print("-" * 56)

candidatos = dados[rotulos == -1]
print("  Viagem candidata (passageiros, atraso) : "
      + str(candidatos.tolist()))
print("=" * 56)

# -------------------------------------------------------------
# Explicação
# -------------------------------------------------------------
print(" Explicação — por que a combinação é incomum:")
print("  Nas viagens normais, mais passageiros estão associados")
print("  a atrasos um pouco maiores (32 passageiros, 3 min;")
print("  80 passageiros, 8 min). A viagem [10 passageiros,")
print("  45 min de atraso] foge totalmente desse padrão:")
print("  POUCOS passageiros e MUITO atraso ao mesmo tempo.")
print()
print("  Possíveis causas:")
print("   - Congestionamento: o trânsito parou o ônibus por muito")
print("     tempo, e a baixa lotação indica horário vazio.");
print("   - Acidente: a via ficou bloqueada, atrasando o veículo.");
print("   - Falha mecânica: o ônibus quebrou no caminho e muitos")
print("     passageiros desceram/pegaram outro ônibus.");
print("   - Erro de registro: o atraso pode ter sido digitado")
print("     como 45 em vez de 4-5 minutos.")

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

plt.xlabel("Passageiros")
plt.ylabel("Atraso (minutos)")
plt.title("Viagens de ônibus — Isolation Forest")
plt.legend()
plt.grid(True)
plt.show()