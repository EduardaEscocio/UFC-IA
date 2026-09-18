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


print("media: ", media(tempo_de_resposta))
print("mediana: ", mediana(tempo_de_resposta))
print("primeiro_quartil: ", primeiro_quartil(tempo_de_resposta))
print("terceiro_quartil: ", terceiro_quartil(tempo_de_resposta))
print("iqr: ", iqr(tempo_de_resposta))
print("outliers: ", outliers(tempo_de_resposta))
print("p95: ", p95(tempo_de_resposta))

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
