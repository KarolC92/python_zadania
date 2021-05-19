"""Zadanie 1.12"""

# Napisz grę polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o rozmiarach 10 na 10.
# Użytkownik może wprowadzać komendy zmieniające położenie postaci.
# Po każdym ruchu użytkownik powinien otrzymywać informację o tym, czy zmierza dobrym kierunku.
# Wyjście poza planszę oznacza koniec gry.
# Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez użytkownika na dojście do celu.
# Dodatkowo:
# - po wykonaniu większej liczby kroków niż dwukrotność minimalnej liczby kroków umieść skarb w nowym miejscu,
# - z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówki po wykonaniu kroku.

# ETAP 1 - ruch po planszy
# 1. zdefiniowane zmienne z pozycją gracza i skarbu (na razie wpisać z palca)
# 2. trzeba zrobić nieskończoną petle while, gdzie:
# - Pokazujemy pozycje gracza
# - Zapytać gracza o kierunek (w,s,a,d)
# - Zmienic kierunek lub poinformowac, ze kierunek jest nieprawdlowy

# ETAP 2 - Sprawdzanie pozycji gracza
# 1. czy gracz przemiescil sie poza plansze - jesli tak, konczymy gre
# 2. czy pozycja gracza (x,y) sa takie same jak pozycja skarbu (x,y) - jesli tak, komunikat o wygranej i konczymy gre

# ETAP 3 - liczba krokow
# 1. Zdefiniować zmienna przed petla
# 2. Po kazdym ruchu ja zwiekszamy
# 3. Jeżeli gracz wejdzie na skarb, to wysiwetlamy informacje ile ruchow wykonal

# ETAP 4 - podpowiedz cieplo, zimno
# http://matematyka.pisz.pl/strona/1248.html
# 1. Policzyc odleglosc miedzy pozycja gracza a skarbu PRZED wykonaniem ruchu.
# 2. Po wykonaniu ruchu znow liczymy odleglosc
# 3. Na podstawie roznicy tych dwoch wartosci mowimy czy cieplo czy zimno.

# ETAP 5 - nie wyswietlaj podpowiedzi cieplo/zimno z prawdopodobienstwem 1/5
# 1. uzywamy randint(1,5) i jezeli wylosuje liczbe inna niz 5, to pokazuje podpowiedz

# ETAP 6 - przeniesienie skarbu po wykonaniu zbyt duzej liczby ruchow
# 1. Przed petla while liczymy sobie minimalna odleglosc miedzy graczem a skarbem - mozemy uzyc funkcji abs()
# 2. Po wykonaniu ruchu sprawdzamy czy liczba_krokow jest wieksza niz dwukrotnosc mininalnej liczby krokow
# 3. jezeli tak jest, to:
#  - losujemy nowa pozycje skarbu (x,y),
#  - liczymy na nowo minimalna liczbe krokow
#  - zerujemy liczbe wykonanych przez gracza krokow

# ETAP 7 - losowanie pozycji gracza i pozycji skarbu na samym poczatku gry
# 1. Dodać randint przy tworzeniu zmiennych przed petla while

import math
import random

gracz_x = random.randint(0, 10)
gracz_y = random.randint(0, 10)
skarb_x = random.randint(0, 10)
skarb_y = random.randint(0, 10)

dystans_1 = math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)

kierunki = ['w', 's', 'd', 'a']
kroki = 0
wynik = 0
min_krok = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

while True:
    dystans_2 = math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)
    print(f'Pozycja gracza: {gracz_x}, {gracz_y}')
    kierunek = input("Podaj kierunek (w, s, d, a): ")
    if kierunek in kierunki:
        if kierunek == 'w':
            gracz_y += 1
        elif kierunek == 's':
            gracz_y -= 1
        elif kierunek == 'd':
            gracz_x += 1
        else:
            gracz_x -= 1
    else:
        print("Podałeś nieprawidłowy kierunek")

    kroki += 1

    if gracz_x > 10 or gracz_y > 10 or gracz_x < 0 or gracz_y < 0:
        print("Jesteś poza planszą - koniec gry!!!")
        break
    if gracz_x == skarb_x and gracz_y == skarb_y:
        print(f'Znalazłeś skarb!!! - Wygrywasz grę!!!\nLiczba kroków wyniosła: {wynik}')
        break

    if random.randint(1, 5) == 1:
        pass
    else:
        if dystans_2 < dystans_1:
            print("Ciepło")
        else:
            print("Zimno")

    dystans_1 = dystans_2

    if kroki > min_krok * 2:
        print("UWAGA!!!, przekroczyłeś limit kroków. Pozycja skarbu zostaje zmieniona!!!")
        wynik += kroki
        kroki = 0
        skarb_x = random.randint(0, 10)
        skarb_y = random.randint(0, 10)

    print('-' * 60)
