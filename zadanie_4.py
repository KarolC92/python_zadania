"""Zadanie 1.2"""

# Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1,
# wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.
# Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
# Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.

dni_tygodnia = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
a = input("Podaj dzień oddania butów: ").lower()
b = ''

if a in dni_tygodnia:
    czas_naprawy = int(input("Podaj czas naprawy: ").split()[0])
    for i in dni_tygodnia:
        if i == a:
            b = dni_tygodnia[(dni_tygodnia.index(i) + czas_naprawy) % 7]
    print(f'Dzień odebrania butów od szewca to: {b}.')
else:
    print("Niepoprawne dane")

