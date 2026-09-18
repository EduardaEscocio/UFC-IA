import math

tempo_de_resposta = [90, 95, 98, 100, 102, 105, 107, 110, 115, 120, 125, 900]


def media(arr: list[int]):
    accum = 0
    size = len(arr)

    for t in arr:
        accum += t

    return accum / size


def mediana(arr: list[int]):

    arr.sort()
    size = len(arr)

    if size % 2 == 0:
        esq = size // 2 - 1
        dir = size // 2

        return (arr[esq] + arr[dir]) // 2

    return arr[size // 2]


def primeiro_quartil(arr: list[int]):
    pos = len(arr) // 2
    return mediana(arr[:pos])


def terceiro_quartil(arr: list[int]):
    pos = (len(arr) + 1) // 2
    return mediana(arr[pos:])


def iqr(arr):
    return terceiro_quartil(arr) - primeiro_quartil(arr)


def is_outlier(num, arr) -> bool:
    limite_inferior = primeiro_quartil(arr) - 1.5 * iqr(arr)
    limite_superior = terceiro_quartil(arr) + 1.5 * iqr(arr)

    return num < limite_inferior or num > limite_superior


def outliers(arr):
    o = []
    for element in arr:
        if is_outlier(element, arr):
            o.append(element)
    return o


def p95(arr):
    arr = sorted(arr)
    pos = math.ceil(len(arr) * 95 / 100)
    return arr[pos - 1]


a = [3, 5, 7, 8, 12, 14, 21]
b = [10, 11, 12, 13, 14, 15]

print("media: ", media(a))
print("mediana: ", mediana(a))
print("primeiro_quartil: ", primeiro_quartil(a))
print("terceiro_quartil: ", terceiro_quartil(a))
print("iqr: ", iqr(a))
print("outliers: ", outliers(a))
print("p95: ", p95(a))

"""
5. A equipe deveria divulgar a média, a mediana ou o P95 em seu relatório de desempenho? Justifique.

o P95, já que representa que 95% das requisições foram atendidas até aquele tempo de resposta, caso fossem
usadas média ou mediana, a interpretação poderia dar a crer que a latência do sistema estaria melhor do que ele
realmente estava

6. Explique por que uma API pode apresentar boa mediana e, ao mesmo tempo, péssima experiência
para alguns usuários.

como a mediana pega o valor no meio, caso a metade superior dos valores seja muito maior do que a inferior, a
mediana iria reportar um valor ceitável, enquanto em aproximadamente metade das requisições o tempo de resposta
seria alto, piorando assim a experiência.
"""
