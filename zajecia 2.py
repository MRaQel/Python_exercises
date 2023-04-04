# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 10:01:10 2022

@author: Joanna
"""

# Przeanalizuj działanie funkcji wbudowanej range().
# Utwórz listę zawierającą wartości:
# od 0 do 100.
# (b) od 2 do 101
# (c) parzyste od 2 do 100 (dwa sposoby)

# lista = []
# for element in range(0, 101):
#     lista.append(round(float(element),2))
# print(lista)

# liczba = 2.225
# print(round(1,2))

#....................................................

#Ciag Fibonaciego:
# w1 = 0
# w2 = 1

# c_fib = [0, 1]

# for cykl in range(4):
#     temp = w2 #temp od temporary (dodatkowa zmienna)
#     w2 = temp + w1
#     w1 = temp
#     c_fib.append(w2)
    
# print(c_fib)

#....................................................
#inny pomysł:
# w1 = 0
# w2 = 1

# c_fib = [0, 1]

# for cykl in range(4):
#     temp = c_fib[-1]
#     w2 = temp + c_fib[-2]
#     w1 = temp
#     c_fib.append(w2)
    
# print(c_fib)

#....................................................
#Utwórz listę zawierającą co trzecią wartość z przedziału 1-20
# oraz listę zawierającą co drugi wyraz z przedziału 1-20.
# Napisz pętlę która umożliwi Ci utworzenie listy będącej częścią
# wspólną wspomnianych list.

# co2 = []
# co3 = []

# #el jako zmienna "element"
# for el in range(1, 21, 2): #musi być jedynka aby wygenerowac przedzial
#     co2.append(el)

# for el in range(1, 21, 3):
#     co2.append(el)
    
#print(co2, co3)
# wywala: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 1, 4, 7, 10, 13, 16, 19] []

# pusta = []
# for el in co2: #ogladamy kazdy element listy pierwszej co 2
#     print(el)
#     if el in co3: #jesli znajduje się tez w liscie co2
#         wspolna.append(el) #to podmieniamy
# print(wspolna)
# #wywala:
# # 1
# # 3
# # 5
# # 7
# # 9
# # 11
# # 13
# # 15
# # 17
# # 19
# # 1
# # 4
# # 7
# # 10
# # 13
# # 16
# # 19
# # []

# #mozna zapisac to w jednej linijce:
# wspolna = [el2 for el2 in co2 if el2 in co3]
# print(wspolna) #cos jest zle :/

#....................................................
# Przeanalizuj działanie funkcji enumarate().
# Utwórz listę krotek przypisującą numer miesiąca do jego nazwy, 
# wykorzystując funkcję enumerate(). 

# miesiace = ["sty", "lut", "mar", "kwi", "maj"]
# przypo = []

# for index, miesiac in enumerate(miesiace): #enumerate przyjmuje liste i zwraca pare: indeks i wartosc
#     #print(index, miesiac)
#     # wywala:
#     #     0 sty
#     #     1 lut
#     #     2 mar
#     #     3 kwi
#     #     4 maj
#     # print(index + 1, miesiac)
#     #wywala:
#         # 1 sty
#         # 2 lut
#         # 3 mar
#         # 4 kwi
#         # 5 maj
#     przypo.append([index + 1, miesiac]) #append przyjmuje jeden argument
#     print(przypo)
#     # wywala:
#         # [[1, 'sty']]
#         # [[1, 'sty'], [2, 'lut']]
#         # [[1, 'sty'], [2, 'lut'], [3, 'mar']]
#         # [[1, 'sty'], [2, 'lut'], [3, 'mar'], [4, 'kwi']]
#         # [[1, 'sty'], [2, 'lut'], [3, 'mar'], [4, 'kwi'], [5, 'maj']]

#....................................................
#petla while:
# lista_do_petli = [1, 2, 3, 4, 5, 6]
# Utwórz listę lista_po_while, która będzie zawierała wartości
# listy_do_pętli (a) pomniejszone o 1 (b) pomniejszone o 2,
# jeżeli orginalna wartość jest mniejsza lub równa 4.

# lista_do_petli = [10, 20, 30, 40, 50, 60]
# lista_po_while = []

# i = 0
# while i < len(lista_do_petli):
#     print(lista_do_petli[i] - 1)
#        # wywala:
#        #  9
#        #  19
#        #  29
#        #  39
#        #  49
#        #  59
#     lista_po_while.append(lista_do_petli[i] - 1)
#     i = i + 1
# print(lista_po_while)
# # wywala: [9, 19, 29, 39, 49, 59]

#....................................................
# powtorki = [30, 30, 1, 13, 3, 14, 14, 10, 12, 16]
# Znajdź i usuń elementy powtarzające się na liście.

# powtorki = [30, 30, 1, 13, 3, 14, 14, 10, 12, 16]
# bez_powtorek = []
    
# for el in powtorki:
#     print(el)
#     if el not in bez_powtorek: #jezeli element nie jest w bez_powtorek
#         bez_powtorek.append(el) #to dodaj ten element do bez_powtorek
#         #print(bez_powtorek)
# print(bez_powtorek)
# #wywala: [30, 1, 13, 3, 14, 10, 12, 16]
# print(set(powtorki))           #zbior
# # wywala: {1, 3, 10, 12, 13, 14, 16, 30}
# print(len(powtorki))
# #wywala: 10
# print(len(set(powtorki)))
# #wywala: 8

#....................................................
# liczby = [19, 30, 1, 13, 3, 0, 14, 10, 12, 16]
# Znajdź maksymalną wartość na liście
# Znajdź minimalną wartość na liście
# Posortuj listę od najmniejszych do największych
# Sprawdź czy elementy listy się powtarzają
# Znajdź drugą co do wielkości wartość na liście.

# liczby = [19, 30, 1, 13, 3, 0, 14, 10, 12, 16]
# print(max(liczby))  #wywala: 30
# print(min(liczby))  #wywala: 0

# liczby.sort()   #sort sortuje
# print(liczby)   #wywala: [0, 1, 3, 10, 12, 13, 14, 16, 19, 30]

# s = liczby.sort() #kropka zmienia obiekt-przypisuje sie to co jest po kropce
# print(s)    #wywala: None
# print(liczby[-2])   #wywala: 19

# liczby.sort(reverse=True)   #wywala: [30, 19, 16, 14, 13, 12, 10, 3, 1, 0]
# print(liczby) 

#....................................................

# Znajdź drugą co do wielkoci na licie
# liczby = [19, 30, 1, 13, 3, 0, 14, 10, 12, 16]
# liczby.sort()
# # def nazwa_funkcji(argument1, argument2,…):
# # 	operacje w funkcji
# # 	return zwracana_wartość
# def druga_co_do_wartosci(lista):
#     lista.sort()
#     return lista[-2]
# print(druga_co_do_wartosci(liczby)) #wywala: 19

#....................................................
# Utwórz funkcję, która wszystkie wartości int w liście
# zamienia na float i odwrotnie.
# Przykładowa lista:
# lista1 = [1, 3, 5.2, 41., -2, 3]

# lista1 = [1, 3, 5.2, 41., -2, 3]

# def zamien(lista_liczb):
#     zamienione = []
#     for el in lista_liczb:
#         if type(el) == type(324):   #in typ el jest równy intiger
#             zamienione.append(float(el))
#         elif type(el) == type(324.):
#             zamienione.append(int(el))
#     return zamienione

# print(zamien(lista1)) #wywala: [1.0, 3.0, 5, 41, -2.0, 3.0]

#....................................................
# import math
# sinus = math.sin(90)
# print(sinus)    #wywala wartosc w radianach: 0.8939966636005579
# sinus = math.sin(math.radians(90))
# print(sinus)    #wywala: 1.0, czyli dobrze

# #krotsza opcja:
# from math import sin, radians
# sinus = math.sin(90)
# print(sinus)

#....................................................
# Utwórz funkcję, która przypisuje status P (pełnoletni) 
# lub N (nieletni) w zależności od roku urodzenia.
# lista_wejsciowa = [['Ania', 2020], ['Basia', 2000],
#                    ['Czarek', 1995], ['Dorota', 1968], ['Ela', 2010]]
# Sugerowany output:
# lista o budowie [[imię, status], [imię, status] …]
# słownik o budowie: {'P': [imię, imię…], 'N’: [imię, imię…]}

# lista_wejsciowa = [['Ania', 2020], ['Basia', 2000], ['Czarek', 1995],
#                    ['Dorota', 1968], ['Ela', 2010]]
# #{'P': [imię, imię…], 'N': [imię, imię…]}    #budowa: nazwa klucza, dwukropek, zmienne

# def przyporzadkuj(lista_list):
#     slownik = {"Pelnoletni": [], "Niepelnoletni": []}    
#     for element in lista_list:
#         if 2022 - element[1] >= 18:
#             slownik["Pelnoletni"] += [element[0]]
#         else:
#             slownik["Niepelnoletni"] += [element[0]]
#     return slownik
# print(przyporzadkuj(lista_wejsciowa))
# #wywalilo: {'Pelnoletni': ['Basia', 'Czarek', 'Dorota'],
# #                          'Niepelnoletni': ['Ania', 'Ela']}

#....................................................
# Rekurencje:
#  Utwórz funkcję znajdującą silnię liczby k.

# def silnia(k):
#     i = 1
#     wynik = i
#     while i <= k:
#         wynik = wynik*i
#         i += 1               #to jest to samo co i = i + 1
#     return wynik
# print(silnia(4))            #wywala: 24

# zm = 3
# print(silnia(zm))           #wywala: 6

#....................................................
# Napisz funkcję, która przepisuje słownik na listę. Następnie za jej pomocą przekształć następujące słowniki na listy:
# {'a': 1, ' ': 6, 'c': 1, 'e': 4, 'g': 1, 'p': 1, 'I': 1, 'm': 1, 'l': 3, 'o': 3, 'n': 1, 'i': 4, 's': 2, 't': 2, 'w': 1, 'v': 1}
# {'a': 3, ' ': 6, 'e': 4, 'f': 1, 'i': 1, 'h': 1, 'm': 2, 'o': 2, 's': 3, 'r': 3, 'T': 1, 'v': 1, 'y': 1, 't': 2}
# {'a': 4, ' ': 6, 'C': 1, 'e': 2, 'g': 1, 'i': 1, 'h': 2, 'm': 2, 'L': 1, 'o': 1, 'I': 1, 's': 3, 'r': 2, 'u': 1, 't': 3, 'v': 1, 'y': 2}

# s1 = {'a': 1, ' ': 6, 'c': 1, 'e': 4, 'g': 1, 'p': 1, 'I': 1, 'm': 1, 'l': 3, 'o': 3, 'n': 1, 'i': 4, 's': 2, 't': 2, 'w': 1, 'v': 1}
# s2 = {'a': 3, ' ': 6, 'e': 4, 'f': 1, 'i': 1, 'h': 1, 'm': 2, 'o': 2, 's': 3, 'r': 3, 'T': 1, 'v': 1, 'y': 1, 't': 2}
# s3 = {'a': 4, ' ': 6, 'C': 1, 'e': 2, 'g': 1, 'i': 1, 'h': 2, 'm': 2, 'L': 1, 'o': 1, 'I': 1, 's': 3, 'r': 2, 'u': 1, 't': 3, 'v': 1, 'y': 2}

# #funkcja, która przepisuje słownik na listę:

# def slownik_do_lista(slownik):
#     lista = []
#     for klucz in slownik:
#         lista.append([klucz, slownik[klucz]])
#     return lista
# #print(slownik_do_lista(s1))

# for slownik in [s1, s2, s3]:
#     print(slownik_do_lista(slownik))
#     print(" ")

#....................................................
#Utwórz funkcję znajdującą silnię liczby m.

# def silnia_rekur(m):
#     if m == 1:
#         return m
#     else:
#         print(m, "to jest m")
#         return m*silnia_rekur(m-1)
# print(silnia_rekur(3))
# #wywala:
#     # 3 to jest m
#     # 2 to jest m
#     # 6

#....................................................
#Utwórz skrypt (najlepiej więcej niż jedna funkcja),
# który rozpozna, czy w listach znajdują się wartości
# string czy float. Następnie dla każdego elementu o typie
# float wyznaczony zostanie sinus tej wartości podany z
# dokładnością do 3 miejsc po przecinku i zapisany do nowej listy.

ostatnia = ["chomik", "kot", 3.124, 1., "tata", 2.5, 0.0]

def sprawdz(lista):
    tylko_float = []
    for element in lista:
        if type(element) == type (2.):
            tylko_float.append(element)
    return tylko_float
print(sprawdz(ostatnia))
# wywala: [3.234, 1.0, 2.5, 0.0]

#teraz musimy zwrócić listę z sinusami
from math import sin
def sin3(lista2):
    sinusy = []
    for element in lista2:
        sinusy.append(round(sin(element),3))
    return sinusy
print(sin3(sprawdz(ostatnia)))
#wywala:[0.018, 0.841, 0.598, 0.0]

bez_str = sprawdz(ostatnia)
sinusy = sin3(bez_str)
print(sinusy)
#wywala: [0.018, 0.841, 0.598, 0.0]









