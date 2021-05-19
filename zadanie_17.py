"""Zadanie 2.3"""

# Napisz program, który odczytuje od użytkownika wiele liczb.
# Program powinien wyliczyć i na końcu wypisać następujące statystyki:
# - liczba podanych liczb (ile sztuk),
# - suma,
# - średnia,
# - minimum
# - maksimum

a = []
while True:
    b = input("Podaj liczbę lub zakończ uzupełnianie liczb wpisując: 'koniec': ")
    if b.lower() != 'koniec':
        if b.isdigit():
            a.append(int(b))
    else:
        break
print('-' * 80)

suma = 0
srednia = 0
minimum = a[0]
maximum = a[0]

for i in range(0, len(a)):
    suma += a[i]
    if i < len(a):
        if a[i] < minimum:
            minimum = a[i]
        if a[i] > maximum:
            maximum = a[i]

srednia = suma / len(a)

print(f'Liczba podanych liczb: {len(a)},\n'
      f'Suma podanych liczb: {suma}\n'
      f'Minimalna podana liczba: {minimum}\n'
      f'Maksymalna podana liczba {maximum}\n'
      f'Średnia podanych liczb wynosi: {srednia:.2f}')
