import json

with open("irregular-verbs.json", "r", encoding="utf-8") as plik:
    czasowniki = json.load(plik)

    print(czasowniki[0])