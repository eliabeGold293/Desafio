"""
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____
"""
def proximo_numero(lista):
    if len(lista) < 2:
        return None  # Não é possível prever com menos de 2 números

    # Calcular a diferença entre os números consecutivos
    diferencas = [lista[i] - lista[i - 1] for i in range(1, len(lista))]

    # Verificar se a diferença é constante (progressão aritmética)
    if all(d == diferencas[0] for d in diferencas):
        return lista[-1] + diferencas[0]

    # Verificar se a razão é constante (progressão geométrica)
    if all(lista[i] != 0 and lista[i - 1] != 0 and lista[i] / lista[i - 1] == lista[1] / lista[0] for i in range(1, len(lista))):
        razao = lista[1] / lista[0]
        return lista[-1] * razao

    # Se não for uma progressão aritmética ou geométrica, retornar None
    return None

a = [1, 3, 5, 7]
b = [2, 4, 8, 16, 32, 64]
c = [0, 1, 4, 9, 16, 25, 36]
d = [4, 16, 36, 64]
e = [1, 1, 2, 3, 5, 8]
f = [2, 10, 12, 16, 17, 18, 19]

listas = [a, b, c, d, e, f]

for lista in listas:
    print(f"O próximo número na sequência {lista} é {proximo_numero(lista)}")












