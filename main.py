a = input()
b = int(input())
if a == "tak" and b >= 18:
    print("Hej kociaku")
    a = input()
    b = int(input())
    c = float(input())
    if (a == "tak" and b =="tak") or c:
        a = input()
        b = int(input())
        c = float(input())
        if (a == "tak" and b =="tak") or c:
            print("przystojny jestes")
        else:
            print("dostajesz friendzone szonie")
    else:
        print("wyjdz za mnie")
else:
    print("nie")