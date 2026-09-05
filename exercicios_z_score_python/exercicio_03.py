# =============================================================
# Exercício 3 — Qual leitura é mais incomum?
# =============================================================

temperaturas = [21, 23, 25, 27, 29]
media        = 25
desvio       = 2

print("=" * 50)
print("  Exercício 3 — Qual leitura é mais incomum?")
print("=" * 50)
print(f"  Média: {media} °C   |   Desvio-padrão: {desvio} °C")
print("=" * 50)

z_scores = []

for temp in temperaturas:
    z = (temp - media) / desvio
    z_scores.append((temp, z))
    print(f"  Temperatura: {temp} °C  →  Z = ({temp} - {media}) / {desvio} = {z:+.2f}")

# Identifica o maior |Z| — pode haver empate
z_abs_max   = max(abs(z) for _, z in z_scores)
mais_incomuns = [temp for temp, z in z_scores if abs(z) == z_abs_max]

print("-" * 50)
print(f"\n  Maiores |Z| por valor:")
for temp, z in sorted(z_scores, key=lambda par: abs(par[1]), reverse=True):
    marcador = " <-- mais incomum" if temp in mais_incomuns else ""
    print(f"    {temp} °C  -->  |Z| = {abs(z):.2f}{marcador}")

# Monta texto dinâmico para a interpretação
if len(mais_incomuns) > 1:
    nomes = " e ".join(f"{t} °C" for t in mais_incomuns)
    intro = f"Há um EMPATE: {nomes} são igualmente incomuns (|Z| = {z_abs_max:.2f})."
else:
    t = mais_incomuns[0]
    z_t = next(z for temp, z in z_scores if temp == t)
    intro = f"A leitura mais incomum é {t} °C, com Z = {z_t:+.2f}."

print(f"""
  Interpretação:
  {intro}
  Esses valores são os mais distantes da média ({media} °C)
  em termos de desvios-padrão, ou seja, os mais atípicos.

  O valor central (25 °C) tem Z = 0.00: é a própria média,
  portanto a leitura MAIS comum/esperada do conjunto.

  Como |Z| <= 2 para todos os valores, nenhuma leitura
  é considerada outlier pela regra prática |Z| > 3.
""")
print("=" * 50)
