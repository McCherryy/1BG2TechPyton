# program podajacy nww

a = int(input("podaj pierwsza liczbe z ktorej chcesz wyznaczyc nww__"))
b = int(input("podaj druga liczbe z ktorej chcesz wyznacz nww__"))

while a != b:
    if a > b: a = a - b
    if b > a: b = b - a
print(a)