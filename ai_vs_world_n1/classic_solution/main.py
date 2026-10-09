# SOLUZIONE AUTOMATION SCRIPTING

import csv

with open("../dipendenti.csv", encoding="utf-8-sig", newline="") as file:
    dipendenti = list(csv.DictReader(file, delimiter=";"))

with open("../presenze.csv", encoding="utf-8-sig", newline="") as file:
    presenze = list(csv.DictReader(file, delimiter=";"))

reparti = {}
totali = {}
ore_totali = 0

for dipendente in dipendenti:
    reparti[dipendente["id_dipendente"]] = dipendente["reparto"]

for presenza in presenze:
    reparto = reparti[presenza["id_dipendente"]]
    ore = int(presenza["ore_straordinario"])

    if reparto not in totali:
        totali[reparto] = 0
    totali[reparto] += ore

for reparto, ore in totali.items():
    ore_totali += ore
    print(f"{reparto}: {ore} ore di straordinario")
    # print(f"{reparto}: {ore / 24:.2f} giorni di straordinario")

print(f"totale: {ore_totali}")