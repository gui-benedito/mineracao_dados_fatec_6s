# =============================================================
# Exercício 8 — Vendas de comércio eletrônico (arquivo CSV)
# =============================================================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

dados = pd.read_csv("vendas_ecommerce.csv")

print("=" * 56)
print("  Exercício 8 — Vendas de comércio eletrônico")
print("=" * 56)
print(" Primeiras linhas do arquivo:")
print("-" * 56)
print(dados.head())
print("-" * 56)

# Características do modelo (id_venda NÃO entra no modelo)
caracteristicas = dados[["valor_total", "quantidade_itens",
                         "desconto_percentual"]]

# 3 vendas suspeitas em 20 observações
modelo = IsolationForest(n_estimators=100,
                         contamination=3 / len(dados),
                         random_state=42)

rotulos = modelo.fit_predict(caracteristicas)

# Adiciona os rótulos ao DataFrame
dados["rotulo"] = rotulos

print(" Vendas candidatas a anomalia:")
print("-" * 56)
candidatas = dados[dados["rotulo"] == -1]
print(candidatas[["id_venda", "data", "valor_total",
                  "quantidade_itens", "desconto_percentual"]])
print("=" * 56)

# -------------------------------------------------------------
# Explicação de cada venda sinalizada
# -------------------------------------------------------------
print(" Explicação das vendas sinalizadas:")
print()
for _, venda in candidatas.iterrows():
    print(f"  {venda['id_venda']} — R$ {venda['valor_total']:.2f}, "
          f"{venda['quantidade_itens']} itens, "
          f"{venda['desconto_percentual']}% de desconto")
    print("     -> Sinalizada porque a combinação valor itens x")
    print("        quantidade x desconto destoa das outras vendas")
    print("        (normal: valor até ~420, 1 a 8 itens, até 20%).")
    print()
print("  V011 (R$ 5.800, 1 item, 90%):")
print("     valor altíssimo com desconto máximo. Pode ser")
print("     promoção legítima de item caro, ou ERRO/possível")
print("     fraude (90% de 5.800 = preço final de R$ 580).")
print()
print("  V017 (R$ 35, 25 itens, 0%):")
print("     MUITOS itens com valor BAIXO (média de R$ 1,40/item).")
print("     Parece erro de cadastro ou produto sem preço real.")
print()
print("  V020 (R$ 4.200, 2 itens, 85%):")
print("     Mesmo padrão da V011. Desconto de 85% em pedido caro")
print("     é incomum — merece investigação de promoção real.")

# -------------------------------------------------------------
# Visualização
# -------------------------------------------------------------
plt.figure(figsize=(7, 5))
normal = dados[dados["rotulo"] == 1]
cand = dados[dados["rotulo"] == -1]

plt.scatter(normal["valor_total"], normal["quantidade_itens"],
            color="#2d6cdf", s=80, label="Normal")
plt.scatter(cand["valor_total"], cand["quantidade_itens"],
            color="#e74c3c", s=120, label="Candidata a outlier")

for _, venda in cand.iterrows():
    plt.annotate(venda["id_venda"],
                 (venda["valor_total"], venda["quantidade_itens"]),
                 textcoords="offset points", xytext=(8, 8))

plt.xlabel("Valor total (R$)")
plt.ylabel("Quantidade de itens")
plt.title("Vendas e-commerce — Isolation Forest")
plt.legend()
plt.grid(True)
plt.show()