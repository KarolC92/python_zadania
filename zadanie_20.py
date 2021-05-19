"""Zadanie 2.5 - B"""

# Napisz program zamieniający miejscami w zadanej liście liczb element największy z najmniejszym.
# na wejsciu: [49, 50, 20, 40, 35, 10]
# na wyjsciu: [49, 10, 20, 40, 35, 50]
#
# Jak to zrobimy?
# 1. Musimy znaleźć indeks elementu o największej wartosci
# i indeks elementu o najmniejszej wartości
# 2. Zamiana miejscami elementów z tych indeksów
#
# Wersja B
# 1. Używając funkcji min(), max() znajduje najmniejszą i najwieksza wartosc
# 2. Znajduję indeks tych elementów w liscie
# 3. Zamieniam te elementy miejscami

a = []
while True:
    b = input("Podaj liczbę lub zakończ dodawanie elementów do listy wpisując 'koniec': ")
    if b == 'koniec':
        break
    else:
        a.append(int(b))

print(f'Lista pierwotna: {a}')

min_index = a.index(min(a))
max_index = a.index(max(a))

a[min_index], a[max_index] = a[max_index], a[min_index]

print(f'Lista końcowa: {a}')
