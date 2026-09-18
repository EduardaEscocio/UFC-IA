prob_nenhum = 0.97
custo_nenhum = 0

prob_reparavel = 0.025
custo_reparavel = 5000

prob_perda_total = 0.005
custo_perda_total = 100000

# Q1: Valor esperado do custo anual por cliente
valor_esperado_custo = (prob_nenhum * custo_nenhum) + (prob_reparavel * custo_reparavel) + (prob_perda_total * custo_perda_total)

# Q2: Resultado esperado com prêmio de R$ 900
premio = 900
resultado_esperado = premio - valor_esperado_custo

# Q3: Custo esperado para 5.000 clientes
clientes = 5000
custo_total_esperado = valor_esperado_custo * clientes

print(f"1. Custo esperado por cliente: R$ {valor_esperado_custo:.2f}")
print(f"2. Resultado esperado: R$ {resultado_esperado:.2f}")
print(f"3. Custo total esperado (5.000 clientes): R$ {custo_total_esperado:.2f}")

# 4. Explique por que “perda total” não pode ser ignorada apesar da baixa probabilidade. 
# A "perda total" não pode ser ignorada porque, apesar da probabilidade de apenas 0,5%, ela é o principal motor financeiro de risco da carteira. 
# Multiplicando a probabilidade (0,5%) pelo impacto (R$ 100.000), o evento compõe R$ 500,00 do custo médio de cada cliente.
# Isso significa que a perda total é responsável por 80% do risco financeiro total (R$ 500 de R$ 625), mesmo sendo o evento mais raro.
# Pelo seu fator de alto impacto, a perda total deve ser considerada na análise. 

# 5. Discuta como uma distribuição de cauda longa pode afetar o capital de reserva da empresa.
# Uma distribuição de cauda longa indica que eventos raros, mas de alto impacto, podem ocorrer com maior frequência do que o esperado em uma distribuição normal. 
# Dessa forma, caso houvesse esse tipo de distribução, a empresa precisaria manter um capital de reserva maior para cobrir possíveis perdas extremas, como o exemplo da perda total.