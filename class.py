from random import randint 


x= []
for i in range(10):
    x.append(i)
print(x)
x = [i for i in range(10)]
print(x)


x = []
for i in range(10):
    x.append(i**2)
print(x)
x = [2**i for i in range(10)]
print(x)


x = []
for i in range(10):
    x.append(i**2-10)
print(x)
x = [2**i-10 for i in range(10)]
print(x)


x = []
for i in range(10):
    x.append(randint(1,10))
print(x)
x = [randint(1,10) for _ in range(10)]
print(x)


def szejk(a,b,c):
    hwifhhaiwhfiahwifhaiwfah
    hiwafhiahwf
    wfaifafj
    print(f"{a} {b} {c}")


def pp_kwadratu_1(a:int)->None:
        print(a**2)

def pp_kwadratu_2(a:str)->float:
    return a**2

wynik = pp_kwadratu_2(8)
pp_3_kwadratow = pp_kwadratu_2(2) + pp_kwadratu_2(5)
print(pp_3_kwadratow)


def Hej()->None:
     print("Hejaka!!!!")

Hej()

for _ in range(10):
     Hej()



def cz_moge_zr_tr(a:float, b:float,c:float)->bool:
     if a+b>c and c+b>a and c+a>b:
          return True
     else:
          return False
# ----------------------------------------------------------------------------------------
while True:
     a = float(input("a ="))
     b = float(input("b ="))
     c = float(input("c ="))
     if cz_moge_zr_tr(a,b,c):
          print("Tak")
     else:
          print("Nie")