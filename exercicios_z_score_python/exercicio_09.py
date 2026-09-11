# =============================================================
# Exercício 9 — Comparação entre IQR e Z-Score
# =============================================================

import numpy as np

dados   = [10, 11, 12, 12, 13, 13, 14, 15, 30]
alvo    = 30

# --- IQR ---
q1  = np.percentile(dados, 25)
q3  = np.percentile(dados, 75)
iqr = q3 - q1

lim_inf = q1 - 1.5 * iqr
lim_sup = q3 + 1.5 * iqr

outlier_iqr = alvo < lim_inf or alvo > lim_sup

# --- Z-Score ---
media  = np.mean(dados)
desvio = np.std(dados)    # desvio populacional (ddof=0)

z      = (alvo - media) / desvio
z_abs  = abs(z)

outlier_z = z_abs > 3

print("=" * 55)
print("  Exercício 9 — Comparação entre IQR e Z-Score")
print("=" * 55)
print(f"  Dados  : {dados}")
print(f"  Valor analisado: {alvo}")
print("=" * 55)

# --- Bloco IQR ---
print(f"""
  METODO 1 — IQR (Intervalo Interquartil)
  Q1           : {q1}
  Q3           : {q3}
  IQR          : Q3 - Q1 = {q3} - {q1} = {iqr}
  Limite inf.  : Q1 - 1.5 x IQR = {q1} - {1.5 * iqr} = {lim_inf}
  Limite sup.  : Q3 + 1.5 x IQR = {q3} + {1.5 * iqr} = {lim_sup}
  Valor {alvo} > {lim_sup}?  {"SIM -> OUTLIER pelo IQR" if outlier_iqr else "NAO -> dentro dos limites"}
""")

# --- Bloco Z-Score ---
print(f"""  METODO 2 — Z-Score
  Media        : {media:.2f}
  Desvio-pad.  : {desvio:.2f}
  Z-Score      : ({alvo} - {media:.2f}) / {desvio:.2f} = {z:.2f}
  |Z| > 3?     {"SIM -> INVESTIGAR pelo Z-Score" if outlier_z else f"NAO -> |Z| = {z_abs:.2f} <= 3 (dentro do esperado)"}
""")

# --- Comparação ---
print("-" * 55)
print(f"  {'Criterio':<20} {'Resultado para valor 30':>30}")
print("-" * 55)
print(f"  {'IQR':<20} {'OUTLIER' if outlier_iqr else 'Normal':>30}")
print(f"  {'Z-Score':<20} {'INVESTIGAR' if outlier_z else 'Comum':>30}")
print("-" * 55)

print("""
  Conclusao:
  O IQR sinalizou o valor 30 como OUTLIER.
  O Z-Score nao ultrapassou o limiar de |Z| > 3.

  Por que resultados diferentes para o mesmo dado?

  O IQR e robusto: baseia-se em Q1 e Q3, que ignoram
  os extremos. Por isso o valor 30 se destaca com clareza.

  O Z-Score e sensivel: usa media e desvio-padrao, que
  sao afetados pelo proprio outlier. O valor 30 "infla"
  o desvio-padrao e acaba parecendo menos extremo do que e.

  Tecnicas diferentes analisam o mesmo dado por criterios
  diferentes. Nenhuma e universalmente superior — a escolha
  depende do contexto, da distribuicao e do objetivo da analise.
  Em dados com outliers reais, o IQR tende a ser mais confiavel.
""")
print("=" * 55)
