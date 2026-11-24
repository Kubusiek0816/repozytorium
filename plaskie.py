from math import pi, sqrt

# ------------------------------------------------------------------------------
# POLA
def pp_kwadratu(a:float)->float:
    return a**2

def pp_porstokata(a:float, b:float)->float:
    return a*b

# --- nowe ---
def pp_rownolegloboku(a:float, h:float)->float:
    return a*h

def pp_trapezu(a:float, b:float, h:float)->float:
    return (a+b)*h/2

def pp_trojkata(a:float, h:float)->float:
    return 1/2*a*h

def pp_trojkata_rownobocznego(a:float)->float:
    return a**2*sqrt(3)/4

def pp_kola(r:float)->float:
    return pi*r**2

def pp_rombu_ah(a:float, h:float)->float:
    return a*h

def pp_rombu_ef(e:float, f:float)->float:
    return e*f/2


def legenda_pp()->None:
    print("a -- pp_kwadratu")
    print("b -- pp_porstokata")
    print("c -- pp_rownolegloboku")
    print("d -- pp_trapezu")
    print("f -- pp_trojkata")
    print("g -- pp_trojkata_rownobocznego")
    print("h -- pp_kola")
    print("i -- pp_rombu (a*h)")
    print("j -- pp_rombu (e*f/2)")
    print("e -- Exsit")


def jakie_pp()->None:
    while True:
        legenda_pp()
        inp = input().lower().strip()
        if inp == "e":
            print("Exsit")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} pp_kwadratu = {pp_kwadratu(a)}")
        elif inp == "b": 
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} pp_porstokata = {pp_porstokata(a,b)}")
        elif inp == "c":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla {a} {h} pp_rownolegloboku = {pp_rownolegloboku(a,h)}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            print(f"dla {a} {b} {h} pp_trapezu = {pp_trapezu(a,b,h)}")
        elif inp == "f":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla {a} {h} pp_trojkata = {pp_trojkata(a,h)}")
        elif inp == "g":
            a = float(input("a = "))
            print(f"dla {a} pp_trojkata_rownobocznego = {pp_trojkata_rownobocznego(a)}")
        elif inp == "h":
            r = float(input("r = "))
            print(f"dla {r} pp_kola = {pp_kola(r)}")
        elif inp == "i":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla {a} {h} pp_rombu = {pp_rombu_ah(a,h)}")
        elif inp == "j":
            e = float(input("e = "))
            f = float(input("f = "))
            print(f"dla {e} {f} pp_rombu = {pp_rombu_ef(e,f)}")

            

# ------------------------------------------------------------------------------
# OBWODY
def obw_kwadaru(a:float)->float:
    return 4*a

def obw_prostokata(a:float, b:float)->float:
    return 2*a+2*b

# --- nowe ---
def obw_rownolegloboku(a:float, b:float)->float:
    return 2*a+2*b

def obw_trapezu(a:float, b:float, c:float, d:float)->float:
    return a+b+c+d

def obw_trojkata(a:float, b:float, c:float)->float:
    return a+b+c

def obw_trojkata_rownobocznego(a:float)->float:
    return 3*a

def obw_kola(r:float)->float:
    return 2*pi*r

def obw_rombu(a:float)->float:
    return 4*a


def legenda_obw()->None:
    print("a -- obw_kwadaru")
    print("b -- obw_prostokata")
    print("c -- obw_rownolegloboku")
    print("d -- obw_trapezu")
    print("f -- obw_trojkata")
    print("g -- obw_trojkata_rownobocznego")
    print("h -- obw_kola")
    print("i -- obw_rombu")
    print("e -- zkoncz program")


def jakie_obw()->None:
    while True:
        legenda_obw()
        inp = input().lower().strip()
        if inp == "e":
            print("Exsit")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} obw_kwadaru = {obw_kwadaru(a)}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} obw_prostokata = {obw_prostokata(a,b)}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} obw_rownolegloboku = {obw_rownolegloboku(a,b)}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            print(f"dla {a} {b} {c} {d} obw_trapezu = {obw_trapezu(a,b,c,d)}")
        elif inp == "f":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"dla {a} {b} {c} obw_trojkata = {obw_trojkata(a,b,c)}")
        elif inp == "g":
            a = float(input("a = "))
            print(f"dla {a} obw_trojkata_rownobocznego = {obw_trojkata_rownobocznego(a)}")
        elif inp == "h":
            r = float(input("r = "))
            print(f"dla {r} obw_kola = {obw_kola(r)}")
        elif inp == "i":
            a = float(input("a = "))
            print(f"dla {a} obw_rombu = {obw_rombu(a)}")

# ------------------------------------------------------------------------------

def plaskie()->None:
    while True:
        print("a -- pp fig plaskich")
        print("b -- obw fig plaskich")
        print("e -- Exsit ")
        inp = input().lower().strip()
        if inp == "a":
            jakie_pp()
        elif inp == "b":
            jakie_obw()
        elif inp == "e":
            print("Exsit")
            break

        
