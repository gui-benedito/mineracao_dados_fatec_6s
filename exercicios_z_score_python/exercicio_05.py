# =============================================================
# Exercício 5 — Monitoramento de CPU com classificação
# =============================================================

import numpy as np

cpu = [42, 45, 47, 44, 46, 43, 48, 92]

# Média e desvio-padrão com NumPy
media  = np.mean(cpu)
desvio = np.std(cpu)

print("=" * 55)
print("  Exercício 5 — Monitoramento de CPU com classificação")
print("=" * 55)
print(f"  Leituras de CPU (%) : {cpu}")
print(f"  Média               : {media:.2f} %")
print(f"  Desvio-padrão       : {desvio:.2f} %")
print("-" * 55)
print(f"  {'Leitura':>10}  {'Z-Score':>8}  {'|Z|':>6}  Classificação")
print("-" * 55)

investigar_lista = []

for leitura in cpu:
    z     = (leitura - media) / desvio
    z_abs = abs(z)

    if z_abs > 3:
        classe = ">> INVESTIGAR <<"
        investigar_lista.append(leitura)
    else:
        classe = "   Comum"

    print(f"  {leitura:>8} %  {z:>+8.2f}  {z_abs:>6.2f}  {classe}")

print("-" * 55)

# Resumo
print(f"\n  Resumo:")
print(f"  Total de leituras  : {len(cpu)}")
print(f"  Comuns (|Z| <= 3)  : {len(cpu) - len(investigar_lista)}")
print(f"  A investigar(|Z|>3): {len(investigar_lista)}")

if investigar_lista:
    print(f"  Valores suspeitos  : {investigar_lista}")

print("""
  Interpretação:
  A leitura de 92% de CPU se destaca fortemente das
  demais, que ficam entre 42% e 48%.
  O desvio-padrão, porém, é inflado pela própria
  presença desse valor extremo — efeito típico do
  Z-Score clássico com outliers reais.

  A classificação "Investigar" não implica remoção.
  Questões relevantes antes de qualquer decisão:
    - Houve um processo pesado rodando naquele momento?
    - É um pico isolado ou recorrente?
    - O sistema apresentou lentidão ou falha associada?
  Somente com esse contexto é possível decidir
  se o valor é um erro, um evento real ou um alerta.
""")
print("=" * 55)
