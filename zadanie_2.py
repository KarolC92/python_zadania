"""Zadanie 1.1 - 2"""

# Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1,
# wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.
# Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
# Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.

cena = float(input("Podaj cenę jednego kilograma ziemniaków: ").split()[0])
ile = float(input("Ile kilogramów ziemniaków chcesz kupić?: ").split()[0])
print(f'Cena za {ile} kg ziemniaków wynosi {cena * ile} zł')