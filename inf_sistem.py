from datetime import datetime
import json
class Vozovi:
    def __init__(self,id_voza,vagoni):
        self.id_voza = id_voza
        self.vagoni = vagoni
    def vrijeme_dolaska(self):
        with open("vozovi.json",encoding="utf8") as vozovi_json:
            vozovii_json=json.load(vozovi_json)
        info_vozovi=[]
        for item in vozovii_json:
            for data_item in item['data']:
                info_vozovi.append(data_item["id_voza"], data_item["grad"])
        index = info_vozovi.index(self.id_voza)
        self.grad = info_vozovi[index + 1]
        if self.grad == "Nikšić":
            print("12:04")
        if self.grad == "Sutomore":
            print("08:49")
        if self.grad == "Beograd":
           print("18:20")
        if self.grad == "Bijelo Polje":
           print("17:00")
        

class Zaposleni:
    def __init__(self,ime,pozicija,ugovor,mjesec_zaposlenja):
        self.ime = ime
        self.pozicija = pozicija
        self.ugovor = ugovor #ugovor(0 za neodredjeno, 1 za odredjeno)
        self.mjesec_zaposlenja = mjesec_zaposlenja
    def set_plata(self):
        if self.pozicija == "Mašinovođa":
            self.plata = 600
        if self.pozicija == "Menadzer":
            self.plata = 650
        if self.pozicija == "Mehaničar":
            self.plata = 450
    def produzenje(self):
        if self.ugovor == 0:
            if self.mjesec_zaposlenja == datetime.now().month: #vraća mjesec na engleskom
                print("Produzi ugovor")
            else:
                print("Ugovor zaposlenog ističe", self.mjesec_zaposlenja)
        else:
            print("Zaposlen je za stalno")
    def novogodisnji_bonus(self): #plata za decembar
        if self.pozicija == "Mašinovođa":
            self.plata = 630
        if self.pozicija == "Menadzer":
            self.plata = 700
        if self.pozicija == "Mehaničar":
            self.plata = 480


