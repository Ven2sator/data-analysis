

import csv
import os

DATEINAME = "inventar.csv"
inventar = []

def lade_daten():
    if os.path.exists(DATEINAME):
        with open(DATEINAME, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for zeile in reader:
                zeile["zurückgegeben"] = zeile["zurückgegeben"] == "True"
                inventar.append(zeile)

def speichere_daten():
    with open(DATEINAME, mode="w", newline="", encoding="utf-8") as f:
        feldnamen = ["name", "item", "zurückgegeben"]
        writer = csv.DictWriter(f, fieldnames=feldnamen)
        writer.writeheader()
        for eintrag in inventar:
            writer.writerow(eintrag)

def verleihen():
    name = input("Name der Person: ").strip()
    item = input("Gegenstand: ").strip()
    inventar.append({"name": name, "item": item, "zurückgegeben": False})
    speichere_daten()
    print(f"{item} wurde an {name} verliehen.\n")

def rückgabe():
    item = input("Welcher Gegenstand wird zurückgegeben? ").strip()
    for eintrag in inventar:
        if eintrag["item"].lower() == item.lower() and not eintrag["zurückgegeben"]:
            eintrag["zurückgegeben"] = True
            rückgeber = input("Wer gibt den Gegenstand zurück? ").strip()
            speichere_daten()
            print(f"{item} wurde von {rückgeber} zurückgegeben.\n")
            return
    print(f"{item} wurde nicht als ausgeliehen gefunden oder ist schon zurückgegeben.\n")

def status():
    offen = [e for e in inventar if not e["zurückgegeben"]]
    print(f"Aktuell ausgeliehen: {len(offen)} Gegenstand/Gegenstände")
    for e in offen:
        print(f"- {e['item']} (verliehen an {e['name']})")
    print()

def menü():
    lade_daten()
    while True:
        print("1. Gegenstand verleihen\n2. Gegenstand zurücknehmen\n3. Status anzeigen\n4. Beenden")
        wahl = input("Auswahl: ").strip()
        if wahl == "1":
            verleihen()
        elif wahl == "2":
            rückgabe()
        elif wahl == "3":
            status()
        elif wahl == "4":
            break
        else:
            print("Ungültige Eingabe.\n")

if __name__ == "__main__":
    menü()
