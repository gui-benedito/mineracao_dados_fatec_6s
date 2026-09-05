# =============================================================
# Exercício 1 — Distância em passos de desvio-padrão
# =============================================================

media  = 100
desvio = 5
valor  = 115

# Distância entre o valor e a média
distancia = valor - media

# Quantos desvios-padrão cabem nessa distância
passos = distancia / desvio

# Z-Score
z_score = passos

# Exibição
print("=" * 45)
print("  Exercício 1 — Distância em passos de DP")
print("=" * 45)
print(f"  Média            : {media}")
print(f"  Desvio-padrão    : {desvio}")
print(f"  Valor analisado  : {valor}")
print("-" * 45)
print(f"  Distância (valor - média) : {distancia}")
print(f"  Passos de DP              : {passos}")
print(f"  Z-Score                   : {z_score:.2f}")
print("-" * 45)

# Interpretação em linguagem natural
direcao     = "acima" if z_score >= 0 else "abaixo"
dist_abs    = abs(distancia)
z_abs       = abs(z_score)
is_outlier  = z_abs > 3

print("\n Interpretação:")
print(f"  O valor {valor} está {dist_abs} unidades {direcao} da média ({media}).")
print(f"  Isso equivale a {z_abs:.1f} desvios-padrão {direcao} da média.")
if is_outlier:
    print(f"  Como |Z| = {z_abs:.2f} > 3, o valor É um possível outlier")
    print(f"  e merece investigação — mas não deve ser removido automaticamente.")
elif z_abs == 3:
    print(f"  Como |Z| = {z_abs:.2f} = 3, o valor está exatamente na fronteira")
    print(f"  do critério de outlier. Merece atenção e avaliação de contexto.")
else:
    print(f"  Como |Z| = {z_abs:.2f} < 3, o valor NÃO é considerado outlier")
    print(f"  pela regra prática do Z-Score. Está dentro do intervalo esperado.")
print("=" * 45)
