# =============================================================
# Exercício 8 — Z-Score em um DataFrame
# =============================================================

import pandas as pd
import numpy as np

dados = {
    "Usuario"    : ["ana", "bruno", "carla", "diego", "eva", "fabio"],
    "Requisicoes": [120, 135, 128, 122, 130, 400]
}

df = pd.DataFrame(dados)

# Média e desvio-padrão da coluna Requisicoes
media  = df["Requisicoes"].mean()
desvio = df["Requisicoes"].std(ddof=0)   # desvio populacional

# Cria as colunas Z_Score e Status
df["Z_Score"] = (df["Requisicoes"] - media) / desvio
df["Status"]  = df["Z_Score"].apply(lambda z: "Investigar" if abs(z) > 3 else "Comum")

print("=" * 60)
print("  Exercício 8 — Z-Score em um DataFrame")
print("=" * 60)
print(f"  Média das requisições  : {media:.2f}")
print(f"  Desvio-padrão          : {desvio:.2f}")
print("=" * 60)
print()
print(df.to_string(index=False,
                   formatters={"Z_Score": lambda z: f"{z:+.2f}"}))
print()
print("-" * 60)

# Resumo por Status
contagem = df["Status"].value_counts()
print(f"\n  Resumo:")
for status, qtd in contagem.items():
    print(f"    {status:12}: {qtd} usuario(s)")

# Lista os suspeitos
suspeitos = df[df["Status"] == "Investigar"]
if not suspeitos.empty:
    for _, row in suspeitos.iterrows():
        print(f"\n  Usuario suspeito : {row['Usuario'].capitalize()}")
        print(f"  Requisicoes      : {row['Requisicoes']}")
        print(f"  Z-Score          : {row['Z_Score']:+.2f}")

print("""
  Interpretacao:
  Fabio registrou 400 requisicoes, muito acima dos demais
  (entre 120 e 135). Seu Z-Score elevado indica um
  comportamento estatisticamente atipico no grupo.

  Possiveis explicacoes a investigar:
    - Uso legitimo intenso (ex: automacao, API integrada)?
    - Requisicoes duplicadas por bug no cliente?
    - Atividade suspeita ou abuso da plataforma?

  O dado nao deve ser removido sem contexto.
  O Z-Score apenas sinalizou — a decisao e humana.
""")
print("=" * 60)
