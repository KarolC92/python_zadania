"""Zadanie 2.2"""

# Napisz program, który wczytuje liczbę całkowitą,
# a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`. Np. dla parametru 3 powinno się wypisać:
# ```
#     *
#   * * *
# * * * * *
# ```

a = int(input("Podaj wysokość choinki: "))
for i in range(a):
    print('  ' * (a - 1 - i) + ' *' * (i * 2 + 1))
