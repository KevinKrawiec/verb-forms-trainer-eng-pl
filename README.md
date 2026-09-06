# Trener form czasowników nieregularnych

Konsolowy program do ćwiczenia angielskich czasowników nieregularnych. Wyświetla polskie znaczenie, a użytkownik wpisuje trzy formy odpowiadającego mu czasownika - oddzielone spacjami.

Projekt powstał w trakcie mojej nauki Pythona. Chciałem przećwiczyć wczytywanie danych z pliku JSON i podział logiki na funkcje, a przy okazji zrobić coś, z czego faktycznie korzystam.

## Uruchomienie

Wymagany Python 3.x, bez zewnętrznych bibliotek.

```bash
python verb_trainer.py
```

## Jak to działa

```
Podaj trzy nieregularne formy czasownika stać: stand stood stood
Podaj trzy nieregularne formy czasownika mówić, powiedzieć: say sayed sayed
Źle. Poprawnie: say, said, said
Podaj trzy nieregularne formy czasownika mówić, powiedzieć: say said said
```

Po błędnej odpowiedzi program pokazuje poprawne formy i pyta o **ten sam** czasownik jeszcze raz. Wpisanie złej liczby słów nie kończy rundy - pytanie się powtarza. Wyjście: `q` albo `koniec`.

## Dane

Zbiór 101 amerykańskich czasowników nieregularnych leży w `irregular-verbs.json`, osobno od kodu:

```json
{"pl": "być", "base": ["be"], "past": ["was", "were"], "participle": ["been"]}
```

Wszystkie trzy formy są listami, mimo że tylko część czasowników ma alternatywne odpowiedzi (`be` -> *was / were*). Początkowo `base` trzymałem jako zwykły string ale ujednoliciłem typy - pozwoliło to porównywać wszystkie formy jedną funkcją.

---
ENG:

# Irregular Verb Forms Trainer - English Version
Console-based program for practising English irregular verbs. It displays a Polish meaning and the user types the three forms of the matching verb - separated by spaces.
The project was created while I was learning Python. I wanted to practise reading data from a JSON file and splitting logic into functions, and at the same time build something I actually use.
## How to run
Requires Python 3.x, no external libraries.
```bash
python verb_trainer.py
```
## How it works
```
Podaj trzy nieregularne formy czasownika stać: stand stood stood
Podaj trzy nieregularne formy czasownika mówić, powiedzieć: say sayed sayed
Źle. Poprawnie: say, said, said
Podaj trzy nieregularne formy czasownika mówić, powiedzieć: say said said
```
After a wrong answer the program shows the correct forms and asks about the **same** verb again. Typing the wrong number of words does not end the round - the question simply repeats. To exit: `q` or `koniec`.
## Data
A set of 101 American English irregular verbs is stored in `irregular-verbs.json`, separately from the code:
```json
{"pl": "być", "base": ["be"], "past": ["was", "were"], "participle": ["been"]}
```
All three forms are lists, even though only some verbs have alternative answers (`be` -> *was / were*). At first I kept `base` as a plain string, but unifying the types allowed me to compare all forms with a single function.
