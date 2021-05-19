"""Zadanie 1.11"""

# Napisz program obliczający średnią wartość temperatury w danym tygodniu na podstawie temperatur
# wprowadzonych przez użytkownika.

dni = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
temperatury = []
for i in range(7):
    temperatury.append(float(input("Wprowadź temperaturę dla: " + dni[i] + ': ').split()[0]))

print(f'Średnia temperatura w tygodniu wynosiła: {sum(temperatury) / 7:.1f} stopni.')
