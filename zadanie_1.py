"""Zadanie 1.1 - 1"""

# Napisz program, który prosi użytkownika (przez `input()`), żeby podał,
# ile kosztuje kilo ziemniaków. Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.
# Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
# ile kosztuje kilo ziemniaków i ile kilo chce kupić. Niech program policzy i wyświetli,
# ile trzeba będzie zapłacić za te ziemniaki.
# Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
# ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
# I niech program sprawdzi i powie,
# za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.

cena = float(input("Podaj cenę ziemniaków: ").split()[0])
print(f'Cena za 5 kg ziemniaków wynosi {cena * 5} zł')