"""Zadanie 1.1 - 2"""

# Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
# ile kosztuje kilo ziemniaków i ile kilo chce kupić. Niech program policzy i wyświetli,
# ile trzeba będzie zapłacić za te ziemniaki.

cena = float(input("Podaj cenę jednego kilograma ziemniaków: ").split()[0])
ile = float(input("Ile kilogramów ziemniaków chcesz kupić?: ").split()[0])
print(f'Cena za {ile} kg ziemniaków wynosi {cena * ile} zł')