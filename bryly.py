from math import pi


# ------------------------------------------------------------------------------
# POLE POWIERZCHNI
def pc_szescianu(a:float)->float:
    return 6*a**2

def pc_prostopadloscianu(a:float, b:float, c:float)->float:
    return 2*a*b+2*a*c+2*b*c

def pc_graniastoslupa(Pp:float, Pb:float)->float:
    return 2*Pp+Pb

def pc_ostroslupa(Pp:float, Pb:float)->float:
    return Pp+Pb

def pc_walca(r:float, H:float)->float:
    return 2*pi*r**2+2*pi*r*H

def pc_stozka(r:float, l:float)->float:
    return pi*r**2+pi*r*l

def pc_kuli(r:float)->float:
    return 4*pi*r**2


def legenda_pc()->None:
    print("a -- pc_szescianu")
    print("b -- pc_prostopadloscianu")
    print("c -- pc_graniastoslupa")
    print("d -- pc_ostroslupa")
    print("f -- pc_walca")
    print("g -- pc_stozka")
    print("h -- pc_kuli")
    print("e -- Exsit")


def jakie_pc()->None:
    while True:
        legenda_pc()
        inp = input().lower().strip()
        if inp == "e":
            print("Exsit")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} pc_szescianu = {pc_szescianu(a)}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"dla {a} {b} {c} pc_prostopadloscianu = {pc_prostopadloscianu(a,b,c)}")
        elif inp == "c":
            Pp = float(input("Pp = "))
            Pb = float(input("Pb = "))
            print(f"dla {Pp} {Pb} pc_graniastoslupa = {pc_graniastoslupa(Pp,Pb)}")
        elif inp == "d":
            Pp = float(input("Pp = "))
            Pb = float(input("Pb = "))
            print(f"dla {Pp} {Pb} pc_ostroslupa = {pc_ostroslupa(Pp,Pb)}")
        elif inp == "f":
            r = float(input("r = "))
            H = float(input("H = "))
            print(f"dla {r} {H} pc_walca = {pc_walca(r,H)}")
        elif inp == "g":
            r = float(input("r = "))
            l = float(input("l = "))
            print(f"dla {r} {l} pc_stozka = {pc_stozka(r,l)}")
        elif inp == "h":
            r = float(input("r = "))
            print(f"dla {r} pc_kuli = {pc_kuli(r)}")


# ------------------------------------------------------------------------------
# OBJETOSC
def v_szescianu(a:float)->float:
    return a**3

def v_prostopadloscianu(a:float, b:float, c:float)->float:
    return a*b*c

def v_graniastoslupa(Pp:float, H:float)->float:
    return Pp*H

def v_ostroslupa(Pp:float, H:float)->float:
    return 1/3*Pp*H

def v_walca(r:float, H:float)->float:
    return pi*r**2*H

def v_stozka(r:float, H:float)->float:
    return 1/3*pi*r**2*H

def v_kuli(r:float)->float:
    return 4/3*pi*r**3


def legenda_v()->None:
    print("a -- v_szescianu")
    print("b -- v_prostopadloscianu")
    print("c -- v_graniastoslupa")
    print("d -- v_ostroslupa")
    print("f -- v_walca")
    print("g -- v_stozka")
    print("h -- v_kuli")
    print("e -- Exsit")


def jakie_v()->None:
    while True:
        legenda_v()
        inp = input().lower().strip()
        if inp == "e":
            print("Exsit")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} v_szescianu = {v_szescianu(a)}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"dla {a} {b} {c} v_prostopadloscianu = {v_prostopadloscianu(a,b,c)}")
        elif inp == "c":
            Pp = float(input("Pp = "))
            H = float(input("H = "))
            print(f"dla {Pp} {H} v_graniastoslupa = {v_graniastoslupa(Pp,H)}")
        elif inp == "d":
            Pp = float(input("Pp = "))
            H = float(input("H = "))
            print(f"dla {Pp} {H} v_ostroslupa = {v_ostroslupa(Pp,H)}")
        elif inp == "f":
            r = float(input("r = "))
            H = float(input("H = "))
            print(f"dla {r} {H} v_walca = {v_walca(r,H)}")
        elif inp == "g":
            r = float(input("r = "))
            H = float(input("H = "))
            print(f"dla {r} {H} v_stozka = {v_stozka(r,H)}")
        elif inp == "h":
            r = float(input("r = "))
            print(f"dla {r} v_kuli = {v_kuli(r)}")

# ------------------------------------------------------------------------------

def bryly()->None:
    while True:
        print("a -- pole powierzchni bryl")
        print("b -- objetosc bryl")
        print("e -- Exsit ")
        inp = input().lower().strip()
        if inp == "a":
            jakie_pc()
        elif inp == "b":
            jakie_v()
        elif inp == "e":
            print("Exsit")
            break
