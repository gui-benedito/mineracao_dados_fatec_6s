# =============================================================
# Exercício 2 — Latência de uma conexão de internet
# =============================================================
import numpy as np
from sklearn.ensemble import IsolationForest

# 14 medições: a maioria entre 20 e 70 ms, duas acima de 200 ms
latencia = [
    [22], [35], [28], [45], [60],
    [30], [50], [25], [40], [55],
    [33], [48], [250], [310]
]

dados = np.array(latencia)

# 2 candidatos em 14 observações
modelo = IsolationForest(n_estimators=100,
                         contamination=2 / len(dados),
                         random_state=42)

modelo.fit(dados)
rotulos = modelo.predict(dados)

print("=" * 50)
print("  Exercício 2 — Latência de uma conexão")
print("=" * 50)
print(f"  Medições           : {len(dados)}")
print(f"  Características    : 1 (latência em ms)")
print(f"  Contaminação       : {2/len(dados):.3f}")
print("-" * 50)
print("  # | Latência (ms) | Classificação")
print("-" * 50)
for i, (valor, rotulo) in enumerate(zip(dados[:, 0], rotulos), start=1):
    classe = "normal" if rotulo == 1 else "CANDIDATO A OUTLIER"
    print(f"  {i:>2} | {valor:>12} | {classe}")
print("-" * 50)

candidatos = dados[rotulos == -1][:, 0]
print(f"  Candidatos sinalizados (ms) : {candidatos.tolist()}")
print("=" * 50)

# -------------------------------------------------------------
# Explicação dos candidatos identificados
# -------------------------------------------------------------
print(" Explicação dos candidatos:")
print("  Os valores 250 ms e 310 ms estão muito acima do padrão")
print("  da conexão (20-70 ms). Em um gráfico da distribuição,")
print("  eles ficam isolados na extremidade superior: o Isolation")
print("  Forest consegue separá-los com pouquíssimas divisões,")
print("  por isso são candidatos a anomalia.")
print()
print("  IMPORTANTE: candidato a anomalia ≠ falha confirmada.")
print("  Uma latência alta pode ter causas legítimas como")
print("  sobrecarga do servidor, uso da rede por outro aplicativo")
print("  (download, atualização), horário de pico ou rota")
print("  internacional da conexão.")