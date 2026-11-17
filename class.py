class Uczen:
   liczba_uczniow = 0
   # Zad1
   # Dodaj brakującą metodę i wywołaj ją w konstruktorze. Metoda do liczenia średniej.
   def srednia(self, oceny):
       return sum(oceny) / len(oceny)
   
   def __init__(self, imie, nazwisko) -> None:
       self.imie = imie
       self.nazwisko = nazwisko
       self.oceny_mat = [2,3,4,5,6]
       self.srednia_ocen_mat = self.srednia(self.oceny_mat)
       self.oceny_ang = [5,6,6,6,6,6,6,6]
       self.srednia_ocen_ang = self.srednia(self.oceny_ang)
       Uczen.liczba_uczniow += 1




   def inf(self):
       print(f"imię {self.imie}")
       print(f"nazwisko {self.nazwisko}")
       print(f"matematyka {self.oceny_mat}")
       print(f"średnia matematyka {self.srednia_ocen_mat}")
       print(f"ang {self.oceny_ang}")
       print(f"średnia ang {self.srednia_ocen_ang}")




   # Zad2
   # Dodaj metodę klasową która będzie liczyć ile obiektów stworzono.(zwiększenie licznika/zmienna klasowa)
    @classmethod
   def ile_obiektow(cls):
       return cls.liczba_uczniow



   # Zad3
   # Dodaj metodę, co pozwoli edytować imię. Zmień imię na Alex.
    def zmien_imie(self, nowe_imie):
       self.imie = nowe_imie

   # Zad4
   # Napisz metodę, co kasuje ocenę o podanej wartości.
   # Za pomocą tej metody usuń wszystkie 6.
    def usun_ocene(self, wartosc): 
       self.oceny_mat = [o for o in self.oceny_mat if o != wartosc]
       self.oceny_ang = [o for o in self.oceny_ang if o != wartosc]
       self.srednia_ocen_mat = self.srednia(self.oceny_mat)
       self.srednia_ocen_ang = self.srednia(self.oceny_ang)


# ----------------------------------------------------------------
u1 = Uczen("Jan", "Kowalski")
u2 = Uczen("Anna", "Nowak")
print(Uczen.ile_obiektow())
u1.zmien_imie("Alex")
u1.usun_ocene(6)
u1.inf()
# ----------------------------------------------------------------
