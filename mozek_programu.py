from databazovy_system import DatabazovySystem
import random

class MozekProgramu:

    def __init__(self):
        self.ds = DatabazovySystem()

    def _vytvor_seznam(self, objekt_k_iteraci):
        docasny_seznam = []
        for objekt in objekt_k_iteraci:
            docasny_seznam.append(objekt)
        return docasny_seznam
    
    def _vyber_nahodne_cislo(self, seznam):
        nahodne_cislo = random.randint(1, len(seznam))
        return nahodne_cislo


    def vyber_vsechny_restaurace(self):
        docasny_seznam = []
        vsechny_restaurace = self.ds.vrat_vsechny_restaurace()
        for restaurace in self._vytvor_seznam(vsechny_restaurace):
            docasny_seznam.append(restaurace[0])
        return docasny_seznam

    def vyber_nahodnou_restauraci(self):
        nahodne_cislo = self._vyber_nahodne_cislo(self.vyber_vsechny_restaurace())
        nahodna_restaurace = self.ds.vyber_restauraci_podle_indexu(nahodne_cislo)
        return nahodna_restaurace[0][0]
    
    def vyber_nahodne_jidlo(self):
        nahodne_cislo = self._vyber_nahodne_cislo(self.vyber_vsechny_restaurace())
        nahodna_restaurace = self.ds.vyber_restauraci_podle_indexu(nahodne_cislo)
        nahodna_jidla = self.ds.vyber_jidlo_dle_zvolene_restaurace(nahodne_cislo)
        seznam_jidel = self._vytvor_seznam(nahodna_jidla)
        vyber_z_jidel = self._vyber_nahodne_cislo(seznam_jidel)
        hodnoty = (nahodna_restaurace[0][0], seznam_jidel[vyber_z_jidel - 1][0])
        hodnoty = self._vytvor_seznam(hodnoty)
        return hodnoty