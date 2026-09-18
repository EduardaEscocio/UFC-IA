cancelamento = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0 ]

def calcular_media(cancelamento):
    return sum(cancelamento)/len(cancelamento)

media = calcular_media(cancelamento)
print(f"A média de cancelamentos é: {media}")

# 2° questão: Interprete a média no contexto do negócio. - A média de cancelamentos e 0.3, o que significa que, em média, 30% dos clientes cancelam seus pedidos. 
# Isso indica que a empresa deve investigar as causas dos cancelamentos e implementar estratégias para reduzir essa taxa.

# 3° questão: Quantos clientes cancelaram? - A quantidade de clientes que cancelaram é 6.

# 4° questão:  Se a empresa possui 10.000 clientes com a mesma taxa, quantos cancelamentos seriam esperados? - 3000 cancelamentos seriam esperados.

# 5° questão:  Cite três variáveis que poderiam ajudar um modelo de machine learning a prever o churn. - Três variáveis que poderiam ajudar a prever o churn são:
#  histórico de compras do cliente, frequência de interações com o serviço de atendimento ao cliente e tempo desde a última compra.

# 6° questão: Por que a "mediana" não faz sentido aqui? - O churn é uma variável binária (0 ou 1), nesse caso a mediana não é útil pois ela é simplesmente 0, não
# demonstrando nenhum padrão ou métrica relevante para o negócio.