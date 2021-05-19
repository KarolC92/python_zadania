"""Zadanie 1.3"""

# Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI,
# oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI: wzór,
# interpretację wyników, proszę znaleźć samodzielnie).

masa = float(input("Podaj masę swojego ciała w kg: "))
wzrost = int(input("Podaj swój wzrost w cm: "))

BMI = masa / ((wzrost / 100) ** 2)
a = f'Twoje BMI wynosi: {BMI:.2f}. '

zalecenia = {1: 'Masz niedowagę.',
             2: 'Wartość Twojego BMI jest w normie.',
             3: 'Masz nadwagę.',
             4: 'Posiadasz otyłość I stopnia.',
             5: 'Posiadasz otyłość II stopnia.',
             6: 'Posiadasz otyłość III stopnia.', }

if BMI < 18.5:
    print(a + zalecenia[1])
elif BMI >= 18.5 and BMI < 25:
    print(a + zalecenia[2])
elif BMI >= 25 and BMI < 30:
    print(a + zalecenia[3])
elif BMI >= 30 and BMI < 35:
    print(a + zalecenia[4])
elif BMI >= 35 and BMI < 40:
    print(a + zalecenia[5])
else:
    print(a + zalecenia[6])
