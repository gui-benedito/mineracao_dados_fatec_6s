# =============================================================
# Exercício 7 — Função de interpretação
# =============================================================

def interpretar_z(z):
    """
    Recebe um Z-Score e retorna sua classificação:
      - |Z| > 3  -> Investigar       (prioridade máxima, avaliado primeiro)
      - Z < 0    -> Abaixo da média
      - Z > 0    -> Acima da média
      - Z == 0   -> Na média
    """
    if abs(z) > 3:
        return "Investigar"
    elif z < 0:
        return "Abaixo da média"
    elif z > 0:
        return "Acima da média"
    else:
        return "Na média"


# Valores de teste
valores_z = [-3.5, -1.2, 0, 0.8, 3.7]

print("=" * 48)
print("  Exercício 7 — Função de interpretação")
print("=" * 48)
print(f"  {'Z-Score':>8}   {'|Z|':>6}   Classificação")
print("-" * 48)

for z in valores_z:
    resultado = interpretar_z(z)
    print(f"  {z:>+8.1f}   {abs(z):>6.1f}   {resultado}")

print("-" * 48)

print("""
  Interpretação:
  A função aplica as regras na ordem correta de prioridade:

  1. |Z| > 3 e verificado PRIMEIRO porque um valor pode
     ser simultaneamente acima/abaixo da media E suspeito.
     Ex: Z = -3.5 esta abaixo da media, mas o que importa
     comunicar e que ele merece investigacao.

  2. Z < 0  -> o valor esta abaixo da media.
  3. Z > 0  -> o valor esta acima da media.
  4. Z == 0 -> o valor e exatamente a media.

  Resultados dos valores testados:
    Z = -3.5  : alem de negativo, ultrapassa |Z|>3 -> Investigar
    Z = -1.2  : moderadamente abaixo da media -> normal
    Z =  0.0  : exatamente na media -> referencia central
    Z = +0.8  : levemente acima da media -> normal
    Z = +3.7  : muito acima da media -> Investigar
""")
print("=" * 48)
