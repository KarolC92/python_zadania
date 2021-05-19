"""Zadanie 2.5 - A"""

# Napisz program zamieniający miejscami w zadanej liście liczb element największy z najmniejszym.
# na wejsciu: [49, 50, 20, 40, 35, 10]
# na wyjsciu: [49, 10, 20, 40, 35, 50]
# Jak to zrobimy?
# 1. Musimy znaleźć indeks elementu o największej wartosci
# i indeks elementu o najmniejszej wartości
# 2. Zamiana miejscami elementów z tych indeksów
#
# Wersja A
# 1. używamy pętli for do znalezienia indeksów, patrz zadanie basics/zad_14
# 2. Zamieniamy wartości pod tymi indeksami

a = []
while True:
    b = input("Podaj liczbę lub zakończ dodawanie elementów do listy wpisując 'koniec': ")
    if b == 'koniec':
        break
    else:
        a.append(int(b))

minimum = a[0]
min_index = 0
maximum = a[0]
max_index = 0

print(f'Lista pierwotna: {a}')

for i in range(len(a)):
    if a[i] < minimum:
        mininimum = a[i]
        min_index = i
    if a[i] > maximum:
        maximum = a[i]
        max_index = i

a[min_index], a[max_index] = a[max_index], a[min_index]

print(f'Lista końcowa: {a}')
