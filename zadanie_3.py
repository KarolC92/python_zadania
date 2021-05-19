"""Zadanie 1.1 - 3"""

# Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
# ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
# I niech program sprawdzi i powie,
# za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.

cena_z = float(input("Podaj cenę kilograma ziemniaków: ").split()[0])
ile_z = float(input("Ile kilogramów ziemniaków chcesz kupić?: ").split()[0])
cena_b = float(input("Podaj cenę kilograma bananów: ").split()[0])
ile_b = float(input("Ile kilogramów bananów chcesz kupić: ").split()[0])
porownanie = ''

if cena_z * ile_z > cena_b * ile_b:
    porownanie = 'Więcej zapłacisz za ziemniaki'
elif cena_z * ile_z < cena_b * ile_b:
    porownanie = 'Więcej zapłacisz za banany'
else:
    porownanie = 'Zapłacisz tyle samo za oba produkty'

print(f'Cena za wszystkie produkty wynosi {cena_z * ile_z + cena_b * ile_b} zł.\n{porownanie}.')
