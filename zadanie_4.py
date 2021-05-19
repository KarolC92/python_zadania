"""Zadanie 1.2"""

dni_tygodnia = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
a = input("Podaj dzień oddania butów: ").lower()
b = ''

if a in dni_tygodnia:
    czas_naprawy = int(input("Podaj czas naprawy: ").split()[0])
    for i in dni_tygodnia:
        if i == a:
            b = dni_tygodnia[(dni_tygodnia.index(i) + czas_naprawy) % 7]

print(f'Dzień odebrania butów od szewca to: {b}.')