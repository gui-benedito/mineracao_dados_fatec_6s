# =============================================================
# Exercício 2 — Acima ou abaixo da média?
# =============================================================

casos  = [85, 100, 120]
media  = 100
desvio = 10

print("=" * 50)
print("  Exercício 2 — Acima ou abaixo da média?")
print("=" * 50)
print(f"  Média: {media}   |   Desvio-padrão: {desvio}")
print("=" * 50)

for valor in casos:
    z = (valor - media) / desvio

    # Define posição em relação à média
    if z > 0:
        posicao = "ACIMA da média"
        sinal   = "positivo → valor maior que a média"
    elif z < 0:
        posicao = "ABAIXO da média"
        sinal   = "negativo → valor menor que a média"
    else:
        posicao = "EXATAMENTE na média"
        sinal   = "zero → valor igual à média"

    print(f"\n  Valor : {valor}")
    print(f"  Z-Score: ({valor} - {media}) / {desvio} = {z:.2f}")
    print(f"  Posição: {posicao}")
    print(f"  Sinal  : {sinal}")
    print("-" * 50)

# Explicação geral dos sinais
print("""
  Significado do sinal do Z-Score:

  Z > 0  → O valor está ACIMA da média.
            Quanto maior o Z, mais distante (para cima).

  Z < 0  → O valor está ABAIXO da média.
            Quanto menor (mais negativo), mais distante (para baixo).

  Z = 0  → O valor É a própria média.
            Nenhum desvio em relação ao centro da distribuição.

  O sinal indica DIREÇÃO; o valor absoluto indica MAGNITUDE.
""")
print("=" * 50)
