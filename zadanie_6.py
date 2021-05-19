"""Zadanie 1.4"""

# Napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza,
# ile trzeba zapłacić. Zasady są takie:
# - nieletni (poniżej 18 roku życia) płacą 100 zł za noc
# - dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
# 	- 200 zł za noc, jeśli nocują jedną noc
# 	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
# 	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
#   - emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
# Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy,
# zapłaci 150 zł za noc z 10% zniżki, czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.

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
