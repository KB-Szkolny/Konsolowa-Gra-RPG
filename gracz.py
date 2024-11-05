class Gracz:
    def __init__(self, pz, atak, obrona):
        self.max_pz = pz
        self.pz = pz
        self.atak = atak
        self.obrona = obrona
        self.zloto = 1000
        
    def atak_przeciwnik(self, przeciwnik):
        przeciwnik.pz = max(0, przeciwnik.pz-self.atak)
        print(f"Zadajesz {self.atak} obrażeń {przeciwnik.imie}owi. Pozostałe życie: {przeciwnik.pz}/{przeciwnik.max_pz}")
    
    def bronienie(self, przeciwnik):
        obrazenia = max(0, przeciwnik.atak - self.obrona)
        self.pz = max(0, self.pz - obrazenia)
        print(f"Tarcza blokuje {self.obrona} obrażeń.\n{przeciwnik.imie} zadaje {obrazenia} obrażeń Graczowi. Pozostałe życie: {self.pz}/{self.max_pz}")

    def leczenie(self):
        self.pz = min(self.max_pz, self.pz + 50)
        print(f"Używasz potki. Pozostałe życie: {self.pz}/{self.max_pz}")