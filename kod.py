from math import pi, sqrt

print("Bryly - a | Plaskie - b | Inne - c")
inp = input("inp: ").lower().strip()

if inp == "a":
    print("ppBryl - a | vBryl - b")
    inp = input("inp: ").lower().strip()

    if inp == "a":
        print("ppSzescianu - a | ppProstopadloscianu - b | ppGraniastoslupa - c | ppOstroslupa - d")
        print("ppWalca - e | ppStozka - f | ppKuli - g")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"ppSzescianu o boku {a} = {6*a**2}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"ppProstopadloscianu o bokach {a} {b} {c} = {2*a*b+2*b*c+2*c*a}")
        elif inp == "c":
            Pp = float(input("Pp (pole podstawy) = "))
            Pb = float(input("Pb (pole powierzchni bocznej) = "))
            print(f"ppGraniastoslupa o Pp={Pp} i Pb={Pb} = {2*Pp+Pb}")
        elif inp == "d":
            Pp = float(input("Pp (pole podstawy) = "))
            Pb = float(input("Pb (pole powierzchni bocznej) = "))
            print(f"ppOstroslupa o Pp={Pp} i Pb={Pb} = {Pp+Pb}")
        elif inp == "e":
            r = float(input("r = "))
            H = float(input("H = "))
            print(f"ppWalca o r={r} i H={H} = {2*pi*r**2+2*pi*r*H}")
        elif inp == "f":
            r = float(input("r = "))
            l = float(input("l (tworzaca) = "))
            print(f"ppStozka o r={r} i l={l} = {pi*r**2+pi*r*l}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"ppKuli o promieniu {r} = {4*pi*r**2}")
        else:
            print("Nie ma takiej komendy")

    elif inp == "b":
        print("vSzescianu - a | vProstopadloscianu - b | vGraniastoslupa - c | vOstroslupa - d")
        print("vWalca - e | vStozka - f | vKuli - g")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"vSzescianu o boku {a} = {a**3}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"vProstopadloscianu o bokach {a} {b} {c} = {a*b*c}")
        elif inp == "c":
            Pp = float(input("Pp (pole podstawy) = "))
            H = float(input("H = "))
            print(f"vGraniastoslupa o Pp={Pp} i H={H} = {Pp*H}")
        elif inp == "d":
            Pp = float(input("Pp (pole podstawy) = "))
            H = float(input("H = "))
            print(f"vOstroslupa o Pp={Pp} i H={H} = {Pp*H/3}")
        elif inp == "e":
            r = float(input("r = "))
            H = float(input("H = "))
            print(f"vWalca o r={r} i H={H} = {pi*r**2*H}")
        elif inp == "f":
            r = float(input("r = "))
            H = float(input("H = "))
            print(f"vStozka o r={r} i H={H} = {pi*r**2*H/3}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"vKuli o promieniu {r} = {4/3*pi*r**3}")
        else:
            print("Nie ma takiej komendy")

    else:
        print("Nie ma takiej komendy")

elif inp == "b":
    print("obwody fig plaskich - a | pp fig plaskich - b")
    inp = input("inp: ").lower().strip()

    if inp == "a":
        print("oKwadratu - a | oProstokata - b | oRownolegloboku - c | oTrapezu - d")
        print("oTrojkata - e | oTrojkataRownobocznego - f | oKola - g | oRombu - h")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"oKwadratu o boku {a} = {4*a}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"oProstokata o bokach {a} {b} = {2*a+2*b}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"oRownolegloboku o bokach {a} {b} = {2*a+2*b}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            print(f"oTrapezu o bokach {a} {b} {c} {d} = {a+b+c+d}")
        elif inp == "e":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"oTrojkata o bokach {a} {b} {c} = {a+b+c}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"oTrojkataRownobocznego o boku {a} = {3*a}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"oKola o promieniu {r} = {2*pi*r}")
        elif inp == "h":
            a = float(input("a = "))
            print(f"oRombu o boku {a} = {4*a}")
        else:
            print("Nie ma takiej komendy")

    elif inp == "b":
        print("pKwadratu - a | pProstokata - b | pRownolegloboku - c | pTrapezu - d")
        print("pTrojkata - e | pTrojkataRownobocznego - f | pKola - g | pRombu - h")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"pKwadratu o boku {a} = {a**2}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"pProstokata o bokach {a} {b} = {a*b}")
        elif inp == "c":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"pRownolegloboku o a={a} i h={h} = {a*h}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            print(f"pTrapezu o a={a} b={b} h={h} = {(a+b)*h/2}")
        elif inp == "e":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"pTrojkata o a={a} i h={h} = {a*h/2}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"pTrojkataRownobocznego o boku {a} = {a**2*sqrt(3)/4}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"pKola o promieniu {r} = {pi*r**2}")
        elif inp == "h":
            print("pRombu z a i h - a | pRombu z przekatnych - b")
            inp = input("inp: ").lower().strip()
            if inp == "a":
                a = float(input("a = "))
                h = float(input("h = "))
                print(f"pRombu o a={a} i h={h} = {a*h}")
            elif inp == "b":
                e = float(input("e = "))
                f = float(input("f = "))
                print(f"pRombu o przekatnych {e} {f} = {e*f/2}")
            else:
                print("Nie ma takiej komendy")
        else:
            print("Nie ma takiej komendy")

    else:
        print("Nie ma takiej komendy")
elif inp == "c":
    print("hTrojkataRownobocznego - a | dKwadratu - b | Pitagoras (przeciwprostokatna) - c")
    inp = input("inp: ").lower().strip()
    if inp == "a":
        a = float(input("a = "))
        print(f"hTrojkataRownobocznego o boku {a} = {a*sqrt(3)/2}")
    elif inp == "b":
        a = float(input("a = "))
        print(f"dKwadratu o boku {a} = {a*sqrt(2)}")
    elif inp == "c":
        a = float(input("a = "))
        b = float(input("b = "))
        print(f"Przeciwprostokatna dla a={a} i b={b}: c = {sqrt(a**2+b**2)}")
    else:
        print("Nie ma takiej komendy")

else:
    print("Nie ma takiej komendy")