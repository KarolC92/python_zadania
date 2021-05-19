"""Zadanie 1.5"""

# Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
# (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
# Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
# Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem.

import math

boki = []
for i in range(3):
    boki.append(float(input(f'podaj długość boku {i + 1}: ')))

if max(boki) < sum(boki) - max(boki):
    p = (sum(boki) / 2)
    wynik = math.sqrt(p * (p - boki[0]) * (p - boki[1]) * (p - boki[1]))
    print(f'Pole tego trójkąta wynosi: {wynik:.2f} j^2')
else:
    print('Z tych boków nie da się zbudować trójkąta')
