import json
import random

def read_file():
    with open("irregular-verbs.json", "r", encoding="utf-8") as f:
        verbs = json.load(f)
        return verbs

def check(answer, correct_answer):
    return answer in correct_answer

def ask(verbs):
    verb = random.choice(verbs)

    while True:
        user_answer = input(f"Podaj trzy nieregularne formy czasownika {verb["pl"]}: ").lower()
        if user_answer == "q" or user_answer == "koniec":
            return False

        parts = user_answer.split()

        if len(parts) != 3:
            print("Podaj 3 formy oddzielone spacją!")
            continue

        a, b, c = parts

        if check(a, verb["base"]) and check(b, verb["past"]) and check(c, verb["participle"]):
            return True

        print(f"Źle. Poprawnie: {' / '.join(verb["base"])}, {' / '.join(verb["past"])}, {' / '.join(verb["participle"])}")

if __name__ == "__main__":
    verbs = read_file()
    while ask(verbs):
        pass