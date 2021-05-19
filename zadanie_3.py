"""Zadanie 1.1 - 3"""

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
