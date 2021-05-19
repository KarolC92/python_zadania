"""Zadanie 2.4"""

# Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
# Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała.
# Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując,
# w której próbie udało się zgadnąć liczbę.
# Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa się bisekcją
# i pełni w informatyce bardzo ważną rolę.
# Umiejętnie ją stosując powinno się te zagadki rozwiązywać w 9-10 próbach (bo 2^10=1024).

import random

a = random.randint(0, 1000)
b = 0
proby = 0
while b != a:
    b = int(input("Zgadnij liczbę z zakresu od 0 do 999: "))
    proby += 1
    if b > a:
        print(f'podana liczba: {b} jest za duża!')
    elif b < a:
        print(f'podana liczba: {b} jest za mała!')
    else:
        print(f'Wygrałeś!!! Poprawna liczba to: {b}. Liczba Twoich prób wynosi: {proby}')
