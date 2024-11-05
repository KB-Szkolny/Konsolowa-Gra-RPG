class Przeciwnik:
    def __init__(self, imie, pz, atak, zloto):
        self.imie = imie
        self.max_pz = pz
        self.pz = pz
        self.atak = atak
        self.zloto = zloto

    def atak_gracz(self, gracz):
        gracz.pz = max(0, gracz.pz - self.atak)
        print(f"{self.imie} zadaje {self.atak} obrażeń Graczowi. Pozostałe życie: {gracz.pz}/{gracz.max_pz}")