from math import sqrt
import funkcje.plaskie as pl
import funkcje.bryly as br

# ------------------------------------------------------------------------------
# WARUNKI (wzory dodatkowe z zielonych kafelkow)
def h_trojkata_rownobocznego(a:float)->float:
    return a*sqrt(3)/2

def przekatna_kwadratu(a:float)->float:
    return a*sqrt(2)

def pitagoras_c(a:float, b:float)->float:
    return sqrt(a**2+b**2)

def pitagoras_a(b:float, c:float)->float:
    return sqrt(c**2-b**2)


def legenda_warunki()->None:
    print("a -- wysokosc trojkata rownobocznego")
    print("b -- przekatna kwadratu")
    print("c -- pitagoras (szukam c)")
    print("d -- pitagoras (szukam a)")
    print("e -- Exsit")


def warunki()->None:
    while True:
        legenda_warunki()
        inp = input().lower().strip()
        if inp == "e":
            print("Exsit")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} h = {h_trojkata_rownobocznego(a)}")
        elif inp == "b":
            a = float(input("a = "))
            print(f"dla {a} d = {przekatna_kwadratu(a)}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} c = {pitagoras_c(a,b)}")
        elif inp == "d":
            b = float(input("b = "))
            c = float(input("c = "))
            if c <= b:
                print("c musi byc wieksze od b")
            else:
                print(f"dla {b} {c} a = {pitagoras_a(b,c)}")


def main():
    print("e - zakoncz program")
    print("a - plaskie")
    print("b - bryly")
    print("c - warunki")
    while True:
        inp = input().lower().strip()
        if inp == "e":
            print("Program zkonczyl dzialanie")
            break
        elif inp == "a":
            pl.plaskie()
        elif inp == "b":
            br.bryly()
        elif inp == "c":
            warunki()

# --------------------------------------------------

main()