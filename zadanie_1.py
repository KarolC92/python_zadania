"""Zadanie 1.1 - 1"""

# Napisz program, który prosi użytkownika (przez `input()`), żeby podał,
# ile kosztuje kilo ziemniaków. Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.

cena = float(input("Podaj cenę ziemniaków: ").split()[0])
print(f'Cena za 5 kg ziemniaków wynosi {cena * 5} zł')