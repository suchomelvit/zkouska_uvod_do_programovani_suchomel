#Vizualizace n-cípé hvězdy
#Vít Suchomel, 3. ročník, SGGI
#zimní semestr 2025/26
#Úvod do programování

import turtle
import math

max_cipu = 50
max_polomer = 400

class Hvezda:

    #Třída reprezentující n-cípou hvězdu.
    #Definuje parametry a umožňuje vykreslení pomocí želví grafiky.

    def __init__(self, pocet_cipu, polomer_opsane, polomer_napojeni):

        #Funkce inicializuje parametry hvězdy.

        self.n = pocet_cipu
        self.r_vnejsi = polomer_opsane
        self.r_vnitrni = polomer_napojeni

    def nakresli(self):

        #Funkce vykreslí hvězdu do grafického okna.
        #Nejpreve zkontroluje vstupní data (limity a logickou správnost).
        #Poté vypočítá souřadnice bodů pomocí goniometrických funkcí.
        #Nakonec vykreslí hvězdu spojením bodů.
        #Vrací True, pokud vše proběhle správně, jinak False.

        if self.n < 3:
            print("Chyba: Nelze vykreslit hvězdu s méně než třemi cípy")
            return False

        if self.r_vnejsi <= self.r_vnitrni:
            print("Chyba: Polměr opsané kružnice musí být větší než poloměr napojení cípů.")
            return False
        
        if self.n > max_cipu:
             print(f"Chyba: Příliš mnoho cípů. Maximum je {max_cipu}.")
             return False
             
        if self.r_vnejsi > max_polomer:
            print(f"Chyba: Poloměr je příiš velký. Maximuální poloměr je {max_polomer}.")
            return False

        pero = turtle.Turtle()
        pero.speed(0)
        pero.pensize(2)

        pocet_bodu = 2 * self.n

        for i in range(pocet_bodu + 1):
            uhel = i * (2 * math.pi / pocet_bodu)

            if i % 2 == 0:
                aktualni_polomer = self.r_vnejsi
            else:
                aktualni_polomer = self.r_vnitrni
            
            x = aktualni_polomer * math.cos(uhel)
            y = aktualni_polomer * math.sin(uhel)

            if i == 0:
                pero.penup()
                pero.goto(x, y)
                pero.pendown()
            else:
                pero.goto(x, y)

        pero.hideturtle()
        return True

try:
    n = int(input("Zadejte počet cípů (např. 5): "))
    r_vnejsi = float(input("Zadejte poloměr kružnice opsané: "))
    r_vnitrni = float(input("Zadejte poloměr kružnice procházející místem napojení cípů: "))

    zadana_hvezda = Hvezda(n, r_vnejsi, r_vnitrni)          

    if zadana_hvezda.nakresli() == True:
        print("Hvězda nakreslena")
        turtle.done()
except ValueError:
    print("Chyba: Musíte zadat platná čísla.")