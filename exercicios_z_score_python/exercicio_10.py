# =============================================================
# Exercício 10 — Mini análise de eventos de segurança
# =============================================================

import pandas as pd

dados = {
    "Evento"          : ["A", "B", "C", "D", "E", "F", "G"],
    "Tentativas_Login": [3, 4, 2, 5, 3, 4, 40]
}

df = pd.DataFrame(dados)

# Média e desvio-padrão (populacional, ddof=0)
media  = df["Tentativas_Login"].mean()
desvio = df["Tentativas_Login"].std(ddof=0)

# Z-Score de cada evento
df["Z_Score"] = (df["Tentativas_Login"] - media) / desvio

# Classificação
df["Status"] = df["Z_Score"].apply(
    lambda z: ">> INVESTIGAR <<" if abs(z) > 3 else "Normal"
)

print("=" * 62)
print("  Exercício 10 — Mini análise de eventos de segurança")
print("=" * 62)
print(f"  Média de tentativas  : {media:.2f}")
print(f"  Desvio-padrão        : {desvio:.2f}")
print("=" * 62)
print()
print(df.to_string(index=False,
                   formatters={"Z_Score": lambda z: f"{z:+.2f}"}))
print()
print("-" * 62)

# Eventos suspeitos
suspeitos = df[df["Status"] == ">> INVESTIGAR <<"]
print(f"\n  Eventos normais    : {len(df) - len(suspeitos)}")
print(f"  Eventos suspeitos  : {len(suspeitos)}")

if not suspeitos.empty:
    print()
    for _, row in suspeitos.iterrows():
        print(f"  Evento {row['Evento']}:")
        print(f"    Tentativas : {row['Tentativas_Login']}")
        print(f"    Z-Score    : {row['Z_Score']:+.2f}")
        print(f"    Status     : {row['Status']}")

print("""
  Interpretação:
  O Evento G registrou 40 tentativas de login — enquanto
  todos os demais ficaram entre 2 e 5.
  Mesmo com o Z-Score sendo inflado pelo próprio outlier,
  o valor se destaca com clareza estatística.

  Por que esse dado pode ser o mais importante?

  Em segurança da informação, o comportamento incomum
  é frequentemente o sinal mais valioso:
    - Muitas tentativas de login podem indicar ataque
      de força bruta ou credential stuffing.
    - Um único evento atípico pode ser o único rastro
      de uma intrusão bem-sucedida.
    - Remover ou ignorar esse dado seria um erro crítico.

  Aqui, o Z-Score não é usado para limpar dados —
  é usado para PRIORIZAR a investigação.
  O dado "sujo" pode ser exatamente o dado mais real
  e mais importante de toda a análise.
""")
print("=" * 62)
