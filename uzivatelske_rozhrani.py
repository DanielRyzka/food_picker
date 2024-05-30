from mozek_programu import MozekProgramu

class UzivatelskeRozhrani:

    def __init__(self):
        self.mozek = MozekProgramu()

    def vyber_akci(self):
        akce = int(input("Vypis vsechny restaurace - 1\nVyber náhodnou restauraci - 2\nVybrat náhodné jídlo - 3\n"))
        if akce == 1:
            print(self.mozek.vyber_vsechny_restaurace())
        elif akce == 2:
            print(self.mozek.vyber_nahodnou_restauraci())
        elif akce == 3:
            print(self.mozek.vyber_nahodne_jidlo())
