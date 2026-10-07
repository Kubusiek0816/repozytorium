# 1.
numbers = []
# 2.
a = float(input("a ="))
numbers.append(a)
b = float(input("b ="))
numbers.append(b)
c = float(input("c ="))
numbers.append(c)
d = float(input("d ="))
numbers.append(d)
e = float(input("e ="))
numbers.append(e)
# 3.
suma = a + b + c + d + e
print("Suma:", suma)
# 4.
najwieksza = a
if b > najwieksza:
    najwieksza = b
if c > najwieksza:
    najwieksza = c
if d > najwieksza:
    najwieksza = d
if e > najwieksza:
    najwieksza = e
print("Najwieksza liczba:", najwieksza)
# 5.
najmniejsza = a
if b < najmniejsza:
    najmniejsza = b
if c < najmniejsza:
    najmniejsza = c
if d < najmniejsza:
    najmniejsza = d
if e < najmniejsza:
    najmniejsza = e
print("Najmniejsza liczba:", najmniejsza)
# 6.
srednia = suma / 5
print("Srednia", srednia)
# 7.
parzyste = 0

reszta_a = a - (a // 2) * 2
if reszta_a == 0:
    parzyste = parzyste + 1

reszta_b = b - (b // 2) * 2
if reszta_b == 0:
    parzyste = parzyste + 1

reszta_c = c - (c // 2) * 2
if reszta_c == 0:
    parzyste = parzyste + 1

reszta_d = d - (d // 2) * 2
if reszta_d == 0:
    parzyste = parzyste + 1

reszta_e = e - (e // 2) * 2
if reszta_e == 0:
    parzyste = parzyste + 1

print("Ilosc liczb parzystych:", parzyste)
# 8.
duplicates = []
if numbers.count(a) > 1 and a not in duplicates:
    duplicates.append(a)
if numbers.count(b) > 1 and b not in duplicates:
    duplicates.append(b)
if numbers.count(c) > 1 and c not in duplicates:
    duplicates.append(c)
if numbers.count(d) > 1 and d not in duplicates:
    duplicates.append(d)
if numbers.count(e) > 1 and e not in duplicates:
    duplicates.append(e)
print("Powtarzajace sie liczby", duplicates)
# 9.
bez_powtorzen = []
if a not in bez_powtorzen:
    bez_powtorzen.append(a)
if b not in bez_powtorzen:
    bez_powtorzen.append(b)
if c not in bez_powtorzen:
    bez_powtorzen.append(c)
if d not in bez_powtorzen:
    bez_powtorzen.append(d)
if e not in bez_powtorzen:
    bez_powtorzen.append(e)
numbers = bez_powtorzen
print("Lista bez powtorzen", bez_powtorzen)
# 10.
squares = []
squares.append(a * a)
squares.append(b * b)
squares.append(c * c)
squares.append(d * d)
squares.append(e * e)
print("Kwadraty liczb", squares)