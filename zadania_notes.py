"""Zadanie 1.1 - 1"""

# cena = float(input("Podaj cenę ziemniaków: "))
# print(f'Cena za 5 kg ziemniaków wynosi {cena*5} zł')

"""Zadanie 1.1 - 2"""

# cena = float(input("Podaj cenę jednego kilograma ziemniaków: "))
# ile = float(input("Ile kilogramów ziemniaków chcesz kupić?: "))
# print(f'Cena za {ile} kg ziemniaków wynosi {cena*ile} zł')

"""Zadanie 1.1 - 3"""

# cena_z = float(input("Podaj cenę kilograma ziemniaków: "))
# ile_z = float(input("Ile kilogramów ziemniaków chcesz kupić?: "))
# cena_b = float(input("Podaj cenę kilograma bananów: "))
# ile_b = float(input("Ile kilogramów bananów chcesz kupić: "))
# porownanie = ''
#
# if cena_z * ile_z > cena_b * ile_b:
#     porownanie = 'Więcej zapłacisz za ziemniaki'
# elif cena_z * ile_z < cena_b * ile_b:
#     porownanie = 'Więcej zapłacisz za banany'
# else:
#     porownanie = 'Zapłacisz tyle samo za oba produkty'
#
# print(f'Cena za wszystkie produkty wynosi {cena_z * ile_z + cena_b * ile_b} zł.\n{porownanie}')

"""Zadanie 1.2"""

# dni_tygodnia = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
# a = input("Podaj dzień oddania butów: ").lower()
# b = ''
# if a in dni_tygodnia:
#     czas_naprawy = int(input("Podaj czas naprawy: "))
#     for i in dni_tygodnia:
#         if i == a:
#             b = dni_tygodnia[(dni_tygodnia.index(i) + czas_naprawy) % 7]
# print(f'Dzień odebrania butów od szewca to: {b}')

"""Zadanie 1.3"""

# masa = float(input("Podaj masę swojego ciała w kg: "))
# wzrost = int(input("Podaj swój wzrost w cm: "))
#
# BMI = masa/((wzrost/100)**2)
# a = f'Twoje BMI wynosi: {BMI:.2f}. '
#
# zalecenia = {1: 'Masz niedowagę.',
#              2: 'Wartość Twojego BMI jest w normie.',
#              3: 'Masz nadwagę.',
#              4: 'Posiadasz otyłość I stopnia.',
#              5: 'Posiadasz otyłość II stopnia.',
#              6: 'Posiadasz otyłość III stopnia.',}
#
# if BMI < 18.5:
#     print(a + zalecenia[1])
# elif BMI >= 18.5 and BMI < 25:
#     print(a + zalecenia[2])
# elif BMI >= 25 and BMI < 30:
#     print(a + zalecenia[3])
# elif BMI >= 30 and BMI < 35:
#     print(a + zalecenia[4])
# elif BMI >= 35 and BMI < 40:
#     print(a + zalecenia[5])
# else:
#     print(a + zalecenia[6])

"""Zadanie 1.4"""

# wiek = int(input("Podaj swój wiek: "))
# ile_nocy = int(input("podaj ile nocy spędzisz w hotelu: "))
# cena = 0
#
# if wiek < 18:
#     cena = ile_nocy * 100
# elif wiek >= 18:
#     if ile_nocy == 1:
#         cena = 200
#     elif ile_nocy > 1 and ile_nocy < 5:
#         cena = ile_nocy * 180
#     else:
#         cena = ile_nocy * 150
# if wiek >= 65:
#     cena = 0.9 * cena
#
# print(f'Kwota, którą zapłacisz za pobyt w hotelu wynosi: {cena:.2f} zł')

"""Zadanie 1.5"""

# import math
#
# boki = []
# for i in range(3):
#     boki.append(float(input(f'podaj długość boku {i+1}: ')))
#
# if max(boki) < sum(boki) - max(boki):
#     p = (sum(boki)/2)
#     wynik = math.sqrt(p * (p-boki[0]) * (p-boki[1]) * (p-boki[1]))
#     print(f'Pole tego trójkąta wynosi: {wynik:.2f} j^2')
# else:
#     print('Z tych boków nie da się zbudować trójkąta')

"""Zadanie 1.6"""

# p = [[[x for x in range(0, 6)], 0],
#              [[x for x in range(6, 18)], 2.28],
#              [[x for x in range(18, 65)], 3.80],
#              [[x for x in range(65, )], 1.90]]
# cena = 0
#
# wiek = int(input('Podaj wiek: '))
# liczba = int(input('Ile potrzebujesz biletów: '))
#
# i = 0
# while True:
#     if wiek in p[i][0]:
#         cena = liczba * p[i][1]
#         break
#     i += 1
#
# print(f'Cena biletów wynosi {cena:.2f} zł')

"""Zadanie 1.7"""

# p_1 = 'Co chcesz kupić? '
# p_2 = 'Podaj cenę towaru '
# p_3 = 'Podaj ilość towaru '
#
# l_z = {p_1: 0,
#        p_2: 0,
#        p_3: 0
#        }
#
# for k in l_z:
#     l_z[k] = input(k)
#
# cena = float(l_z[p_2].split()[0]) * float(l_z[p_3].split()[0])
# print(f'Za {l_z[p_1]}, które chcesz kupić zapłacisz: {cena:.2f} zł')

"""Zadanie 1.8"""

# imie = input("Podaj imię psa: ")
# wiek = int(input("Podaj wiek psa: "))
# print(f'Gdyby {imie} był człowiekiem, miałby {wiek * 5} lat.')

"""Zadanie 1.9"""

# for i in range(1, 101):
#     if i % 15 == 0:
#         print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)

"""Zadanie 1.10"""

# boki = []
# wynik = 1
# porownanie = ''
#
# for i in range(3):
#     boki.append(int(input(f'Podaj w cm bok {i+1}: ')))
#     wynik *= boki[i]
#
# if wynik > 1000:
#     porownanie = 'większa od objętości'
# elif wynik == 1000:
#     porownanie = 'taka sama jak objętość'
# else:
#     porownanie = 'mniejsza od objętości'
#
# print(f'Objętość opakowania wynosi {wynik} cm i jest ona {porownanie} 1 litra')

"""Zadanie 1.11"""

# dni = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
# temperatury = []
# for i in range(7):
#     temperatury.append(float(input("Wprowadź temperaturę dla: " + dni[i] + ': ').split()[0]))
#
# print(f'Średnia temperatura w tygodniu wynosiła: {sum(temperatury)/7:.1f} stopni')

"""Zadanie 1.12"""

# import math
# import random
#
# gracz_x = random.randint(0, 10)
# gracz_y = random.randint(0, 10)
# skarb_x = random.randint(0, 10)
# skarb_y = random.randint(0, 10)
#
# dystans_1 = math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)
#
# kierunki = ['w', 's', 'd', 'a']
# kroki = 0
# wynik = 0
# min_krok = abs(skarb_x-gracz_x) + abs(skarb_y-gracz_y)
#
# while True:
#     dystans_2 = math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)
#     print(f'Pozycja gracza: {gracz_x}, {gracz_y}')
#     kierunek = input("Podaj kierunek (w, s, d, a): ")
#     if kierunek in kierunki:
#         if kierunek == 'w':
#             gracz_y += 1
#         elif kierunek == 's':
#             gracz_y -= 1
#         elif kierunek == 'd':
#             gracz_x += 1
#         else:
#             gracz_x -= 1
#     else:
#         print("Podałeś nieprawidłowy kierunek")
#
#     kroki += 1
#
#     if gracz_x > 10 or gracz_y > 10 or gracz_x < 0 or gracz_y < 0:
#         print("Jesteś poza planszą - koniec gry!!!")
#         break
#     if gracz_x == skarb_x and gracz_y == skarb_y:
#         print(f'Znalazłeś skarb!!! - Wygrywasz grę!!!\nLiczba kroków wyniosła: {wynik}')
#         break
#
#     if random.randint(1, 5) == 1:
#         pass
#     else:
#         if dystans_2 < dystans_1:
#             print("Ciepło")
#         else:
#             print("Zimno")
#
#     dystans_1 = dystans_2
#
#     if kroki > min_krok*2:
#         print("UWAGA!!!, przekroczyłeś limit kroków. Pozycja skarbu zostaje zmieniona!!!")
#         wynik += kroki
#         kroki = 0
#         skarb_x = random.randint(0, 10)
#         skarb_y = random.randint(0, 10)
#
#     print('-' * 60)

"""Zadanie 2.1"""

# import random
#
# a = random.randint(9, 99)
# b = random.randint(9, 99)
# answer = False
# while not answer:
#     result = int(input(f'Podaj sumę liczb {a} oraz {b}: '))
#     if result == a + b:
#         answer = True
#         print('Poprawna odpowiedź')
#     else:
#         print('Niepoprawna odpowiedź')

"""Zadanie 2.2"""

# a = int(input("Podaj wysokość choinki: "))
# for i in range(a):
#     print('  ' * (a - 1 - i) + ' *' * (i * 2 + 1))

"""Zadanie 2.3"""

# a = []
# while True:
#     b = input("Podaj liczbę lub zakończ uzupełnianie liczb wpisując 'koniec': ")
#     if b.lower() != 'koniec':
#         if b.isdigit():
#             a.append(int(b))
#     else:
#         break
#
# suma = 0
# srednia = 0
# minimum = a[0]
# maximum = a[0]
#
# for i in range(0, len(a)):
#     suma += a[i]
#     if i < len(a):
#         if a[i] < minimum:
#             minimum = a[i]
#         if a[i] > maximum:
#             maximum = a[i]
#
# srednia = suma/len(a)
#
# print(f'Liczba podanych liczb: {len(a)},\n'
#       f'Suma podanych liczb: {suma}\n'
#       f'Minimalna podana liczba: {minimum}\n'
#       f'Maksymalna podana liczba {maximum}\n'
#       f'Średnia podanych liczb wynosi: {srednia}')

"""Zadanie 2.4"""

# import random
#
# a = random.randint(0, 1000)
# b = 0
# proby = 0
# while b != a:
#     b = int(input("Zgadnij liczbę z zakresu od 0 do 999: "))
#     proby += 1
#     if b > a:
#         print(f'podana liczba: {b} jest za duża!')
#     elif b < a:
#         print(f'podana liczba: {b} jest za mała!')
#     else:
#         print(f'Wygrałeś!!! Poprawna liczba to: {b}. Liczba Twoich prób wynosi: {proby}')

"""Zadanie 2.5 - A"""

# a = [49, 50, 20, 40, 35, 10]
# minimum = a[0]
# min_index = 0
# maximum = a[0]
# max_index = 0
# for i in range(len(a)):
#     if a[i] < minimum:
#         mininimum = a[i]
#         min_index = i
#     if a[i] > maximum:
#         maximum = a[i]
#         max_index = i
#
# a[min_index], a[max_index] = a[max_index], a[min_index]
# print(a)

"""Zadanie 2.5 - B"""

# a = [49, 50, 20, 40, 35, 10]
# min_index = a.index(min(a))
# max_index = a.index(max(a))
#
# a[min_index], a[max_index] = a[max_index], a[min_index]
# print(a)