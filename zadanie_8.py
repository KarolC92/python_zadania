"""Zadanie 1.6"""

# Założenia:
# 	- 0-6   - wiek przedszkolny - cena biletu: 0
# 	- 7-17  - wiek szkolny      - cena biletu: 2.28
# 	- 18-64 - wiek dorosły      - cena biletu: 3.80
# 	- +65   - wiek emerytalny   - cena biletu: 1.90
# Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
# Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić. Wczytywanie danych
# i ich wyświetlenie zrealizuj za pomocą konsoli.

p = [[[x for x in range(0, 6)], 0],
     [[x for x in range(6, 18)], 2.28],
     [[x for x in range(18, 65)], 3.80],
     [[x for x in range(65, )], 1.90]]

cena = 0
wiek = int(input('Podaj wiek: ').split()[0])
liczba = int(input('Ile potrzebujesz biletów: '))

i = 0
while True:
    if wiek in p[i][0]:
        cena = liczba * p[i][1]
        break
    i += 1

print(f'Cena biletów wynosi {cena:.2f} zł')
