# Trener form czasowników nieregularnych

Konsolowy program do ćwiczenia angielskich czasowników nieregularnych. Wyświetla polskie znaczenie, a użytkownik wpisuje trzy formy odpowiadającego mu czasownika — oddzielone spacjami.

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

Po błędnej odpowiedzi program pokazuje poprawne formy i pyta o **ten sam** czasownik jeszcze raz. Wpisanie złej liczby słów nie kończy rundy — pytanie się powtarza. Wyjście: `q` albo `koniec`.

## Dane

Zbiór 101 amerykańskich czasowników nieregularnych leży w `irregular-verbs.json`, osobno od kodu:

```json
{"pl": "być", "base": ["be"], "past": ["was", "were"], "participle": ["been"]}
```

Wszystkie trzy formy są listami, mimo że tylko część czasowników ma alternatywne odpowiedzi (`be` → *was / were*). Początkowo `base` trzymałem jako zwykły string ale ujednoliciłem typy - pozwoliło porównywać wszystkie formy jedną funkcją.
