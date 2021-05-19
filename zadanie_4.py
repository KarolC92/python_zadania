"""Zadanie 1.2"""

# Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza,
# ile trzeba zapłacić. Zasady są takie:
# - nieletni (poniżej 18 roku życia) płacą 100 zł za noc
# - dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
# 	- 200 zł za noc, jeśli nocują jedną noc
# 	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
# 	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
# - emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
# Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy,
# zapłaci 150 zł za noc z 10% zniżki, czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.

dni_tygodnia = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
a = input("Podaj dzień oddania butów: ").lower()
b = ''

if a in dni_tygodnia:
    czas_naprawy = int(input("Podaj czas naprawy: ").split()[0])
    for i in dni_tygodnia:
        if i == a:
            b = dni_tygodnia[(dni_tygodnia.index(i) + czas_naprawy) % 7]
    print(f'Dzień odebrania butów od szewca to: {b}.')
else:
    print("Niepoprawne dane")

