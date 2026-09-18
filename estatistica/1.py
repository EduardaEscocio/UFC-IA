numeros = [3200, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4200, 25000]

def calcular_media(numeros):
    return sum(numeros)/len(numeros)

def calcular_mediana(numeros):
    n = len(numeros)
    if n % 2 == 0:
        mediana = (numeros[n//2 - 1] + numeros[n//2]) / 2
    else:
        mediana = numeros[n//2] 
    return mediana
    
media = calcular_media(numeros)
mediana = calcular_mediana(numeros)

print(f"A média é: {media}")
print(f"A mediana é: {mediana}")

# 3° questão Existe moda? Justifique - Não tem moda na questão, nenhum valor se repete mais de uma vez, logo não há moda.

# 5° questão: Qual medida representa melhor o salário típico dos funcionários? - A mediana representa melhor o 
# salário típico dos funcionários, pois é menos sensível a valores extremos em relação à média.

# 6° questão: Explique como uma empresa poderia usar apenas a média para produzir uma interpretação enganosa. 
# Uma empresa poderia usar apenas a média para criar uma impressão equivocada sobre o salário típico dos funcionários, especialmente se houver valores extremos 
# que distorçam a média, fazendo parecer que os funcionários ganham mais do que realmente fazem.

# Apresente os cálculos e escreva uma conclusão de até cinco linhas destinada ao setor de Recursos - 
# 2. Cálculo da Média:
# Soma de todos os valores: 3200 + 3400 + 3500 + 3600 + 3700 + 3800 + 3900 + 4000 + 4200 + 25000 = 58300
# Média = Soma / n
# Média = 58300 / 10 = 5830

# 3. Cálculo da Mediana:
# Como n = 10 (par), a mediana é a média dos dois valores centrais (5º e 6º elementos).
# 5º elemento = 3700
# 6º elemento = 3800
# Mediana = (3700 + 3800) / 2 = 3750

# Conclusão para o setor de Recursos Humanos:

# A média de 5830 não reflete a realidade da equipe, pois está severamente distorcida por um salário atípico (25000), de um cargo mais elevado.
#  A mediana de 3750 é a métrica mais confiável e representativa para o padrão de remuneração da maioria dos colaboradores.
#  Portanto, o RH deve utilizar a mediana
#  como base principal para análises de mercado e padrões salariais.