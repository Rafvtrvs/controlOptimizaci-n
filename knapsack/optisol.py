import timeit
import seaborn as sns
import matplotlib.pyplot as plt
import random
import pandas as pd

# C : capacidad total de la mochila.
# p : Peso por objeto i.
# v : Valor por objeto i.
# n : cantidad de objetos.

# memoria para almacenar soluciones {C,n} en un diccionario.

memoria = {}

def Mochila(p, v, n, C):

    # se define el caso base (cuando no quedan objetos ni capacidad)

    if n == 0 or C == 0:
        return 0

    # si el ultimo objeto considerado excede la capacidad de la mochila...
    # llama recursivamente la función sin ese objeto.

    if (p[n - 1] > C):
        return Mochila(p, v, n - 1, C)

    # Revisar si la solución del subproblema ya se encuentra memoizado.

    if (C, n) in memoria:
        return memoria[(C, n)]

    # si se toma el valor actual, suma su valor, resta la capacidad total y llama recursivamente la función sin tomar en cuenta ese objeto.

    valor_tomado = v[n - 1] + Mochila( p, v, n - 1, C - p[n-1])

    # si no se toma el objeto actual, llama a la función recursiva sin el objeto actual.

    valor_notomado = Mochila(p, v, n - 1, C)

    # para ambos casos, toma el maximo de esos valores.

    valor_max = max(valor_tomado, valor_notomado)

    # guarda la solución optima en la memoria.

    memoria[(C, n)] = valor_max

    # retorna el valor máximo.

    return valor_max


def Mochila_Bt(p, v, n, C, i=0, p_act=0, v_act=0):

    # Caso base, si recorrimos todos los objetos.

    if i == n:
        return v_act

    # si no toma el objeto actual, avanza al siguiente.
    max_valor = Mochila_Bt(p, v, n, C, i + 1, p_act, v_act)


    # si toma el objeto actual, su peso + el peso acumulado no debe exceder la capacidad total de la mochila.
    # de cumplirse esa condición, avanza al siguiente objeto, acumulando peso y valor.

    if p_act + p[i] <= C:
        max_valor = max(
            max_valor,
            Mochila_Bt(
                p, v, n, C,
                i + 1,
                p_act + p[i],
                v_act + v[i]
            )
        )

    # retorna el maximo valor encontrado.

    return max_valor

import timeit

instancias = [
    {
        "ejemplo": 1,
        "n": 9,
        "p": [6, 4, 8, 4, 3, 5, 5, 1, 1],
        "v": [6, 12, 18, 19, 4, 3, 17, 3, 15],
        "C": 25
    },
    {
        "ejemplo": 2,
        "n": 9,
        "p": [8, 2, 3, 5, 7, 4, 4, 1, 3],
        "v": [4, 17, 14, 12, 12, 9, 10, 20, 7],
        "C": 26
    },
    {
        "ejemplo": 3,
        "n": 7,
        "p": [6, 8, 9, 9, 8, 6, 4],
        "v": [18, 6, 17, 12, 13, 10, 14],
        "C": 13
    },
    {
        "ejemplo": 4,
        "n": 10,
        "p": [7, 1, 8, 5, 8, 5, 3, 3, 1, 9],
        "v": [17, 18, 14, 12, 2, 11, 1, 14, 1, 19],
        "C": 12
    },
    {
        "ejemplo": 5,
        "n": 9,
        "p": [9, 2, 4, 4, 10, 7, 10, 3, 5],
        "v": [4, 8, 5, 19, 12, 20, 1, 4, 9],
        "C": 30
    },
    {
        "ejemplo": 6,
        "n": 8,
        "p": [10, 10, 1, 4, 6, 2, 2, 7],
        "v": [16, 17, 7, 3, 12, 17, 8, 2],
        "C": 27
    },
    {
        "ejemplo": 7,
        "n": 7,
        "p": [1, 3, 6, 4, 7, 9, 6],
        "v": [16, 2, 19, 6, 17, 8, 20],
        "C": 28
    },
    {
        "ejemplo": 8,
        "n": 6,
        "p": [7, 8, 2, 5, 6, 10],
        "v": [18, 12, 13, 19, 15, 11],
        "C": 26
    },
    {
        "ejemplo": 9,
        "n": 5,
        "p": [4, 4, 4, 3, 1],
        "v": [17, 4, 9, 1, 9],
        "C": 11
    },
    {
        "ejemplo": 10,
        "n": 9,
        "p": [9, 1, 7, 3, 7, 5, 1, 5, 4],
        "v": [13, 5, 17, 6, 12, 12, 20, 9, 20],
        "C": 26
    }
]

resultados = {
    "DP": [],
    "Backtracking": []
}

for inst in instancias:
    p = inst["p"]
    v = inst["v"]
    C = inst["C"]
    n = inst["n"]
    ejemplo = inst["ejemplo"]

    def ejecutar_dp():
        return Mochila(p, v, n, C)

    tiempo_dp = timeit.timeit(ejecutar_dp, number=1)
    resultado_dp = ejecutar_dp()

    resultados["DP"].append({
        "ejemplo": ejemplo,
        "n": n,
        "C": C,
        "tiempo": tiempo_dp,
        "resultado": resultado_dp
    })

    tiempo_bt = timeit.timeit(lambda: Mochila_Bt(p, v, n, C), number=1)
    resultado_bt = Mochila_Bt(p, v, n, C)

    resultados["Backtracking"].append({
        "ejemplo": ejemplo,
        "n": n,
        "C": C,
        "tiempo": tiempo_bt,
        "resultado": resultado_bt
    })

print("INSTANCIAS GENERADAS")

for inst in instancias:
    print(f"\nEjemplo {inst['ejemplo']}")
    print(f"n: {inst['n']}")
    print(f"Pesos: {inst['p']}")
    print(f"Valores: {inst['v']}")
    print(f"Capacidad: {inst['C']}")

for metodo, lista in resultados.items():
    print(f"\n=== {metodo} ===")
    for r in lista:
        print(
            f"Ejemplo {r['ejemplo']} | "
            f"n={r['n']} | "
            f"C={r['C']} | "
            f"Tiempo: {r['tiempo']:.6f} s | "
            f"Resultado: {r['resultado']}"
        )
