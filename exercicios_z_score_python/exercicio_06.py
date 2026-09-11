# =============================================================
# Exercício 6 — O mesmo valor em dois contextos
# =============================================================

media_a  = 100
desvio_a = 2
media_b  = 100
desvio_b = 20
valor    = 110

# Z-Score nos dois grupos
z_a = (valor - media_a) / desvio_a
z_b = (valor - media_b) / desvio_b

distancia = valor - media_a   # mesma nos dois grupos: 10

print("=" * 55)
print("  Exercício 6 — O mesmo valor em dois contextos")
print("=" * 55)
print(f"  Valor analisado    : {valor}")
print(f"  Distância absoluta : {valor} - {media_a} = {distancia} unidades (igual nos dois grupos)")
print("=" * 55)

# --- Grupo A ---
print(f"""
  GRUPO A
  Média: {media_a}  |  Desvio-padrão: {desvio_a}
  Z = ({valor} - {media_a}) / {desvio_a} = {z_a:.2f}
  |Z| = {abs(z_a):.2f}  ->  {">> INVESTIGAR << (|Z| > 3)" if abs(z_a) > 3 else "Comum (|Z| <= 3)"}
""")

# --- Grupo B ---
print(f"""  GRUPO B
  Média: {media_b}  |  Desvio-padrão: {desvio_b}
  Z = ({valor} - {media_b}) / {desvio_b} = {z_b:.2f}
  |Z| = {abs(z_b):.2f}  ->  {">> INVESTIGAR << (|Z| > 3)" if abs(z_b) > 3 else "Comum (|Z| <= 3)"}
""")

print("-" * 55)
print("  Comparação direta:")
print(f"  {'':20}  {'Grupo A':>10}  {'Grupo B':>10}")
print(f"  {'Desvio-padrão':20}  {desvio_a:>10}  {desvio_b:>10}")
print(f"  {'Distância absoluta':20}  {distancia:>10}  {distancia:>10}")
print(f"  {'Z-Score':20}  {z_a:>+10.2f}  {z_b:>+10.2f}")
print(f"  {'Classificação':20}  {'Investigar':>10}  {'Comum':>10}")
print("-" * 55)

print("""
  Interpretação:
  A distância absoluta é a mesma nos dois grupos: 10 unidades.
  Mas o Z-Score depende do contexto, medido pelo desvio-padrão.

  Grupo A (DP = 2): os dados ficam muito próximos da média.
  Um desvio de 10 unidades representa 5 desvios-padrão —
  algo extremamente raro nesse grupo. Merece investigação.

  Grupo B (DP = 20): os dados variam bastante naturalmente.
  Um desvio de 10 unidades representa apenas 0.5 desvios-padrão
  — perfeitamente comum e esperado nesse contexto.

  Conclusão: o Z-Score não mede distância absoluta.
  Ele mede distância RELATIVA ao comportamento do grupo.
  O mesmo valor pode ser outlier em um contexto e
  absolutamente normal em outro.
""")
print("=" * 55)
