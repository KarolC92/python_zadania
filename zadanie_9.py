"""Zadanie 1.7"""

# Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i jaka jest jego cena.
# Wyświetl odpowiedni komunikat.
# Przykład:
# Co chcesz kupić? - ziemniaki
# Podaj cenę towaru - 5
# Podaj ilość towaru - 10
# Za ziemniaki, który chcesz kupić, zapłacisz 50 zł

p_1 = 'Co chcesz kupić? '
p_2 = 'Podaj cenę towaru '
p_3 = 'Podaj ilość towaru '

l_z = {p_1: 0,
       p_2: 0,
       p_3: 0
       }

for k in l_z:
    l_z[k] = input(k)

cena = float(l_z[p_2].split()[0]) * float(l_z[p_3].split()[0])
print(f'Za {l_z[p_1]}, które chcesz kupić zapłacisz: {cena:.2f} zł')
