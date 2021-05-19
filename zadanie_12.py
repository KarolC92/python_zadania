"""Zadanie 1.10"""

# Napisz program, który na podstawie wprowadzonych wymiarów opakowania (x, y, z) obliczy jego objętość oraz sprawdzi,
# czy jest ona większa od 1 litra (1000 cm3).

boki = []
wynik = 1
porownanie = ''

for i in range(3):
    boki.append(int(input(f'Podaj w cm. bok {i + 1}: ')))
    wynik *= boki[i]

if wynik > 1000:
    porownanie = 'większa od objętości'
elif wynik == 1000:
    porownanie = 'taka sama jak objętość'
else:
    porownanie = 'mniejsza od objętości'

print(f'Objętość opakowania wynosi {wynik} cm i jest ona {porownanie} 1 litra')
