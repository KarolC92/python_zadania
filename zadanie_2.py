"""Zadanie 1.1 - 2"""

cena = float(input("Podaj cenę jednego kilograma ziemniaków: ").split()[0])
ile = float(input("Ile kilogramów ziemniaków chcesz kupić?: ").split()[0])
print(f'Cena za {ile} kg ziemniaków wynosi {cena * ile} zł')