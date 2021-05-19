"""Zadanie 1.4"""

wiek = int(input("Podaj swój wiek: ").split()[0])
ile_nocy = int(input("podaj ile nocy spędzisz w hotelu: "))
cena = 0

if wiek < 18:
    cena = ile_nocy * 100
elif wiek >= 18:
    if ile_nocy == 1:
        cena = 200
    elif ile_nocy > 1 and ile_nocy < 5:
        cena = ile_nocy * 180
    else:
        cena = ile_nocy * 150
if wiek >= 65:
    cena = 0.9 * cena

print(f'Kwota, którą zapłacisz za pobyt w hotelu wynosi: {cena:.2f} zł')
