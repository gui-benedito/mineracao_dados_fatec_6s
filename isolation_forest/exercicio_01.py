# =============================================================
# Exercício 1 — Vendas de uma mercearia (Isolation Forest)
# =============================================================
import numpy as np
from sklearn.ensemble import IsolationForest

vendas = [
    [80], [85], [90], [88],
    [92], [87], [95], [89],
    [91], [400]
]

dados = np.array(vendas)

# Aproximadamente 1 candidato em 10 observações -> contamination = 1/10
modelo = IsolationForest(n_estimators=100,
                         contamination=1/10,
                         random_state=42)

modelo.fit(dados)

# Classificação de todas as vendas (1 = normal, -1 = candidato a outlier)
rotulos = modelo.predict(dados)

print("=" * 50)
print("  Exercício 1 — Vendas de uma mercearia")
print("=" * 50)
print(f"  Observações        : {len(dados)}")
print(f"  Características    : 1 (quantidade vendida)")
print(f"  Contaminação       : 1 em 10 (10%)")
print("-" * 50)
print("  Venda | Classificação")
print("-" * 50)
for valor, rotulo in zip(dados[:, 0], rotulos):
    classe = "normal" if rotulo == 1 else "CANDIDATO A OUTLIER"
    print(f"  {valor:>5} | {classe}")
print("-" * 50)

candidatos = dados[rotulos == -1][:, 0]
print(f"  Valor sinalizado pelo modelo : {candidatos.tolist()}")
print("=" * 50)

# -------------------------------------------------------------
# Explicação
# -------------------------------------------------------------
# Uma venda muito acima do padrão (400 contra ~80-95) pode ser:
#
# 1. Promoção: uma campanha de descontos pode elevar as vendas
#    de um dia específico de forma legítima.
# 2. Encomenda: um cliente (ex.: restaurante, lanchonete) pode
#    ter feito um pedido grande no dia, o que é um evento real.
# 3. Erro de registro: o operador pode ter digitado 400 em vez
#    de 40, ou registrado duas vendas em uma só linha.
#
# O modelo apenas aponta o valor como "diferente do padrão".
# Ele não sabe a CAUSA. Por isso a observação deve ser
# investigada antes de qualquer decisão.

print()
print(" Discussão: o valor 400 deve ser removido automaticamente?")
print("  NÃO. Remover automaticamente é perigoso:")
print("  - Se for uma promoção ou encomenda real, o dado é")
print("    legítimo e carrega informação valiosa sobre o negócio.")
print("  - Se for erro de digitação, o correto é CORRIGIR,")
print("    não simplesmente excluir.")
print("  - A decisão correta é investigar o contexto do dia")
print("    (houve promoção? houve encomenda? quem registrou?)")
print("    e só então decidir entre manter, corrigir ou remover.")
