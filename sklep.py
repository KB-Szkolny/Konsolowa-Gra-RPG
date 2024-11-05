import os
class Sklep:
    def __init__(self):
        self.przedmioty = {
            "Miecz": {"koszt": 50, "atak": 20},
            "Tarcza": {"koszt": 50, "obrona": 20},
            "Leczenie": {"koszt": 50, "leczenie": 50}
        }

    def kup_przedmiot(self, gracz, przedmiot_nazwa):
        if przedmiot_nazwa in self.przedmioty:
            przedmiot = self.przedmioty[przedmiot_nazwa]
            if gracz.zloto >= przedmiot["koszt"]:
                gracz.zloto -= przedmiot["koszt"]
                match przedmiot_nazwa:
                    case "Miecz":
                        gracz.atak += przedmiot["atak"]
                        print(f"Kupiłeś {przedmiot_nazwa}. Twój atak wzrósł o {przedmiot['atak']}. Aktualny atak: {gracz.atak}")
                    case "Tarcza":
                        gracz.obrona += przedmiot["obrona"]
                        print(f"Kupiłeś {przedmiot_nazwa}. Twoja obrona wzrosła o {przedmiot['obrona']}. Aktualna obrona: {gracz.obrona}")
                    case "Leczenie":
                        gracz.leczenie()
            else:
                print("Nie masz wystarczająco złota.")
        else:
            print("Nie ma takiego przedmiotu w sklepie.")