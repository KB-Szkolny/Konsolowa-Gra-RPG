import random
import os
from gracz import Gracz
from przeciwnik import Przeciwnik
from sklep import Sklep


print("Witaj w grze!")
gracz = Gracz(pz=150, atak=80, obrona=40)
sklep = Sklep()
os.system("cls")
while gracz.pz > 0:
    przeciwnicy = [Przeciwnik("Goblin", pz=82, atak=123, zloto=90),
                    Przeciwnik("Ork", pz=140, atak=98, zloto=70),
                    Przeciwnik("Mag", pz=110, atak=134, zloto=75),
                    Przeciwnik("Rycerz", pz=97, atak=114, zloto=120),
                    Przeciwnik("Troll", pz=91, atak=102, zloto=116),
                    Przeciwnik("Elf", pz=87, atak=138, zloto=80),
                    Przeciwnik("Szkielet", pz=77, atak=96, zloto=130)]
    przeciwnik = random.choice(przeciwnicy)
    print(f"W okolicy pojawił się {przeciwnik.imie}!\nGracz: {gracz.pz}/{gracz.max_pz}\n{przeciwnik.imie}: {przeciwnik.pz}/{przeciwnik.max_pz}")

    while przeciwnik.pz > 0 and gracz.pz > 0:
        ruch = input("Co chcesz zrobić?\n1. Atak\n2. Obrona\n3. Sklep\n4. Ucieczka\n")
        match ruch:
            case "1":
                os.system("cls")
                gracz.atak_przeciwnik(przeciwnik)
                if przeciwnik.pz > 0:
                    przeciwnik.atak_gracz(gracz)
            case "2":
                os.system("cls")
                gracz.bronienie(przeciwnik)
            case "3":
                os.system("cls")
                print(f"Witaj w sklepie! Dostępne przedmioty: (Twoje złoto: {gracz.zloto})")
                for przedmiot, szczegoly in sklep.przedmioty.items():
                    print(f"{przedmiot} - koszt: {szczegoly['koszt']} złota")
                przedmiot_nazwa = input("Wpisz nazwę przedmiotu, który chcesz kupić: ")
                sklep.kup_przedmiot(gracz, przedmiot_nazwa)
            case "4":
                os.system("cls")
                print("Ucieczka!")
                break
            case _:
                print("Nieprawidłowa akcja, spróbuj ponownie.")

    if przeciwnik.pz <= 0:
        print(f"Pokonałeś {przeciwnik.imie}!")
        gracz.zloto += przeciwnik.zloto
        print(f"Zdobyłeś {przeciwnik.zloto} złota. Aktualne złoto: {gracz.zloto}")

print("Koniec gry!")
