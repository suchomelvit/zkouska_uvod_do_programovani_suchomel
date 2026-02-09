#Hledání nejkratšího a nejdelšího slova
#Vít Suchomel, 3. ročník, SGGI
#zimní semestr 2025/26
#Úvod do programování

import string

class AnalyzaTextu:

    #Třída pro zpracování a analýzu textového řetězce.
    #Očišťuje vstupní text od interpunkce a číslic.
    #Vyhledává nejdelší a nejkratší slova.

    def __init__(self, zadany_text):

        #Funkce rozděluje text na slova (tokeny).
        #Ukládá očištěná slova do seznamu self.slova

        self.text = zadany_text
        neocistena_slova = zadany_text.split()

        self.slova = []

        znaky_k_orezani = string.punctuation + "0123456789"

        for slovo in neocistena_slova:
            ciste_slovo = slovo.strip(znaky_k_orezani)

            if len(ciste_slovo) > 0 and ciste_slovo.isalpha():
                self.slova.append(ciste_slovo)

    def najdi_nejdelsi(self):

        #Funkce hledá nejdelší slova v seznamu.
        ##Pokud je seznam prázdný, vrací [], 0.

        if not self.slova:
            return [], 0 
        max_delka = max(len(slovo) for slovo in self.slova)
        
        nejdelsi = [slovo for slovo in self.slova if len(slovo) == max_delka]
        return nejdelsi, max_delka

    def najdi_nejkratsi(self):

        #Funkce hledá nejkratší slova v seznamu.
        #Pokud je seznam prázdný, vrací [], 0.

        if not self.slova:
            return [], 0 
        
        min_delka = min(len(slovo) for slovo in self.slova)
        nejkratsi = [slovo for slovo in self.slova if len(slovo) == min_delka]
        
        return nejkratsi, min_delka
    
#Hlavní část programu, zajišťující jeho běh     
    
vlozte_text = input("Vložte text, ve kterém chcete vyhledat nejdelš a nejkratší slovo: ")
analyza = AnalyzaTextu(vlozte_text)

if len(analyza.slova) == 0:
    print("Chyba: Zadal jste neplatný text (žádná platná slova).")

else:

    vysledek_nejdelsi, max_delka = analyza.najdi_nejdelsi()
    vysledek_nejkratsi, min_delka = analyza.najdi_nejkratsi()

    print(f"Analyzovaný text: {vlozte_text}")
    print(f"Nejdelší slovo je/jsou: {vysledek_nejdelsi}. Počet znaků: {max_delka}")
    print(f"Nejkratší slovo je/jsou: {vysledek_nejkratsi}. Počet znaků: {min_delka}")