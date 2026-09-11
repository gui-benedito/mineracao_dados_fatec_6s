# =============================================================
# Exercício 4 — Latência de uma API
# =============================================================

import numpy as np

latencias = [98, 102, 101, 99, 100, 103, 97, 180]
valor_alvo = 180

# Média e desvio-padrão com NumPy
media  = np.mean(latencias)
desvio = np.std(latencias)   # desvio populacional (ddof=0)

# Z-Score apenas da latência 180 ms
z = (valor_alvo - media) / desvio

print("=" * 52)
print("  Exercício 4 — Latência de uma API")
print("=" * 52)
print(f"  Latências (ms) : {latencias}")
print("-" * 52)
print(f"  Média          : {media:.2f} ms")
print(f"  Desvio-padrão  : {desvio:.2f} ms")
print("-" * 52)
print(f"  Valor analisado: {valor_alvo} ms")
print(f"  Z-Score        : ({valor_alvo} - {media:.2f}) / {desvio:.2f} = {z:.2f}")
print("-" * 52)

# Avaliação
z_abs = abs(z)
if z_abs > 3:
    status = "MERECE INVESTIGAÇÃO  (|Z| > 3)"
    emoji  = "!"
else:
    status = "dentro do esperado   (|Z| <= 3)"
    emoji  = "-"

print(f"\n  [{emoji}] |Z| = {z_abs:.2f}  ->  {status}")

print("""
  Interpretação:
  A latência de 180 ms está muito acima das demais,
  que se concentram entre 97 ms e 103 ms.
  Seu Z-Score elevado indica que ela é estatisticamente
  atípica em relação ao padrão observado.

  AVISO IMPORTANTE:
  Investigar NÃO significa apagar automaticamente.
  Antes de qualquer decisão, verifique:
    - Houve sobrecarga momentânea no servidor?
    - Ocorreu algum evento externo (deploy, pico de uso)?
    - A latência alta se repete em outros registros?
  Somente o contexto revela se o valor é erro, fraude
  ou simplesmente um evento real e válido.
""")
print("=" * 52)
