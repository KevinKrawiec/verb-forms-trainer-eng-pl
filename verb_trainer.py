import json
import random

with open("irregular-verbs.json", "r", encoding="utf-8") as plik:
    czasowniki = json.load(plik)

print(czasowniki[0])
print(czasowniki[0]["past"])

while True:
    user_answer = input(f"Podaj 2 forme {czasowniki[0]["pl"]}: ")
    if user_answer in czasowniki[0]["past"]:
        print("dobrze")
        break
    else:
        for v in czasowniki[0].values():
            print(v, end=", ")
        print("\nspróbuj ponownie")