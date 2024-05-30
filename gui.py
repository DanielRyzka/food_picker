import tkinter as tk
from mozek_programu import MozekProgramu 

mp = MozekProgramu()

def vypsat_restauraci_do_listboxu():
    vystupni_okno.delete(0, tk.END)
    vystupni_okno.insert(tk.END, _vybrat_restauraci())
def _vybrat_restauraci():
    restaurace = mp.vyber_nahodnou_restauraci()
    return restaurace

def vypsat_restauraci_jidlo_do_listboxu():
    vybrana_restaurace_jidlo = _vybrat_restauraci_jidlo()
    vystupni_okno.delete(0, tk.END)
    for i in vybrana_restaurace_jidlo:
        vystupni_okno.insert(tk.END, i)    
def _vybrat_restauraci_jidlo():
    restaurace_jidlo = mp.vyber_nahodne_jidlo()
    return restaurace_jidlo

hlavni_okno = tk.Tk()

hlavni_okno.minsize(250,150)
hlavni_okno.config(background="grey")
hlavni_okno.title("Food picker")

vystup_frame = tk.Frame(hlavni_okno, background="grey")
vystup_frame.pack()
tlacitko_frame = tk.Frame(hlavni_okno, background="grey")
tlacitko_frame.pack()

vystupni_okno = tk.Listbox(vystup_frame, width=40, height=5)
vystupni_okno.pack(pady=5)

vybrat_restauraci_tlacitko = tk.Button(tlacitko_frame, text="Vybrat restauraci", background="orange", command= vypsat_restauraci_do_listboxu)
vybrat_restauraci_tlacitko.grid(row=0, column=0, pady=5, padx=2)

vybrat_jidlo_tlacitko = tk.Button(tlacitko_frame, text="Vybrat restauraci + jidlo", background="orange", command=vypsat_restauraci_jidlo_do_listboxu)
vybrat_jidlo_tlacitko.grid(row=0, column=1, pady=5, padx=2)


hlavni_okno.mainloop()
mp.ds.conn.commit()
mp.ds.uzavrit_spojeni()