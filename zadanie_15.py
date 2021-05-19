"""Zadanie 2.1"""

# Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej).
# Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej). Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
# Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.

import random

a = random.randint(9, 99)
b = random.randint(9, 99)
answer = False
while not answer:
    result = int(input(f'Podaj wynik działania: {a} + {b} = '))
    if result == a + b:
        answer = True
        print('Poprawna odpowiedź')
    else:
        print('Niepoprawna odpowiedź')
