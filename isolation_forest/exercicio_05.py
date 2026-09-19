# =============================================================
# Exercício 5 — Regra fixa versus Isolation Forest
# =============================================================
import numpy as np
from sklearn.ensemble import IsolationForest

consumo_agua = [
    [48], [52], [50], [55],
    [49], [53], [51], [54],
    [56], [12], [180]
]

dados = np.array(consumo_agua)

# -------------------------------------------------------------
# Regra fixa (manual)
#   Consumo normal esperado: entre 30 e 100 litros
#   Muito baixo: < 30   |   Muito alto: > 100
# -------------------------------------------------------------
def regra_fixa(valor):
    if valor < 30:
        return "muito BAIXO"
    if valor > 100:
        return "muito ALTO"
    return "normal"

regra = np.array([regra_fixa(v) for v in dados[:, 0]])

# -------------------------------------------------------------
# Isolation Forest (mesma contaminação que a regra sinaliza:
# 2 candidatos em 11 observações)
# -------------------------------------------------------------
modelo = IsolationForest(n_estimators=100,
                         contamination=2 / len(dados),
                         random_state=42)

modelo.fit(dados)
rotulos_if = modelo.predict(dados)  # 1 = normal, -1 = candidato

print("=" * 62)
print("  Exercício 5 — Regra fixa versus Isolation Forest")
print("=" * 62)
print("  Consumo (L) | Regra fixa     | Isolation Forest")
print("-" * 62)
for valor, r, rotulo in zip(dados[:, 0], regra, rotulos_if):
    classe_if = "normal" if rotulo == 1 else "CANDIDATO"
    print(f"  {valor:>10} | {r:<14} | {classe_if}")
print("-" * 62)

cand_regra = sorted(set(dados[regra != "normal"][:, 0].astype(int).tolist()))
cand_if = sorted(set(dados[rotulos_if == -1][:, 0].astype(int).tolist()))

print(f"  Sinalizados pela regra fixa       : {cand_regra}")
print(f"  Sinalizados pelo Isolation Forest : {cand_if}")
print(f"  Candidatos são os mesmos?         : "
      + ("SIM" if cand_regra == cand_if else "NÃO"))
print("=" * 62)

# -------------------------------------------------------------
# Limitações da regra fixa
# -------------------------------------------------------------
print(" Limitações de uma regra fixa:")
print("  - Os limites (30 e 100) foram escolhidos MANUALMENTE e")
print("    são arbitrários: outro analista poderia usar 25 e 120,")
print("    mudando o resultado.");
print("  - A regra não se adapta: se o consumo médio subir para")
print("    80 L ao longo do tempo, o limite de 100 continua o")
print("    mesmo e passa a sinalizar (ou deixar passar) errado.");
print("  - Só enxerga extremos simples (muito alto / muito baixo).")
print("    Não detecta padrões mais sutis ou combinações de")
print("    características (por exemplo: consumo normal, mas em")
print("    horário impossível).")

# -------------------------------------------------------------
# Vantagem do Isolation Forest
# -------------------------------------------------------------
print()
print(" Por que o Isolation Forest ajuda quando NÃO existe um")
print(" limite definido previamente:")
print("  - O modelo APRENDE o padrão dos próprios dados: ele")
print("    encontra o que é 'normal' comparando isoladamente cada")
print("    observação com o restante.");
print("  - Não precisa que o analista adivinhe números de corte.");
print("  - Adapta-se a mudanças: se o consumo normal mudar, o")
print("    modelo recalcula o que é padrão e o que foge dele.")