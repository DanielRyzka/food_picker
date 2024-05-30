import sqlite3

class DatabazovySystem:

    def __init__(self):
        self.conn = sqlite3.connect("databaze_restauraci.db")
        self.cur = self.conn.cursor()

    def vrat_vsechny_restaurace(self):
        restaurace = self.cur.execute("SELECT nazev_restaurace FROM 'restaurace'")
        return restaurace.fetchall()
    
    def vrat_vsecny_nabidky(self):
        nabidka = self.cur.execute("SELECT jidla FROM nabidka")
        return nabidka.fetchall()
    
    def vyber_restauraci_podle_indexu(self, index):
        vybrana_restaurace = self.cur.execute("SELECT nazev_restaurace FROM restaurace WHERE id_restaurace = ?", (index,))
        return vybrana_restaurace.fetchall()

    def vyber_jidlo_dle_zvolene_restaurace(self, index):
        vybrana_jidla = self.cur.execute("SELECT jidla FROM nabidka WHERE restaurace_id = ?", (index,))
        return vybrana_jidla.fetchall()

    def uzavrit_spojeni(self):
        self.conn.close()


