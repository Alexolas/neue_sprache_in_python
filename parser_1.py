import random
class Parser:
    def __init__(self):

        self._messages = []

    def parse(self, code):
        for zeile in code.split("\n"):


            if zeile.startswith("help") and len(zeile.rstrip()) < 5:
                self._messages.append(help_text)
            elif zeile.startswith("say "):
                said_text = zeile[3:len(zeile)]
                self._messages.append(said_text.lstrip()+"\n")
            elif zeile.startswith("listanimals") or zeile.startswith("listAnimals") and len(zeile.rstrip()) == 11:
                self._messages.append("Liste:")
                for l in list_animals:
                    self._messages.append("\n- " + l)
                self._messages.append("\n\n")
            elif zeile.startswith("randomAnimal") or zeile.startswith("randomanimal") and len(zeile.rstrip()) > 11:
                if len(zeile.rstrip()) == 12:
                    self._messages.append(random.choice(list_animals))
                else:
                    if "," not in zeile:
                        self._messages.append("Die Tiernamen werden durch Kommata getrennt.")
                        return False
                    if zeile.startswith("randomAnimal"):
                        list = ''.join(zeile.split("randomAnimal "))
                    else:
                        list = ''.join(zeile.split("randomanimal "))
                    for t in list.split(","):
                        if t.strip() not in list_animals:
                            self._messages.append("Mindestens ein Tiername existiert nicht. Wähle zwischen:\n- " + '\n- '.join(list_animals))
                            return False
                    e = random.choice(list.split(","))
                    self._messages.append(e.strip() + "\n")
            else:
                self._messages.append("Du hast wahrscheinlich einen Befehl falsch eingegeben. Versuche es mit 'help' für die Liste der Befehle.")
                return False
        return True

# randomAnimal Alpaka,Hase,Tiger,Schwein
# Ausgabe vielleicht: Hase

list_animals = ['Alpaka','Esel','Hase','Hund','Katze','Krokodil','Kuh','Löwe',
'Panda','Salamander','Schaf','Schwein','Tiger']

help_text = """say\n- fast gleiche Aufgabe wie print("") in Python 
- gibt durch Leerzeichen zu trennende Wörter aus\n- gibt folgende Zeichen wieder(a - z, A - Z, 0 - 9, alle
 alle Zeichen)\n- z.B.\n<say Hallo09\n\nmake\n- erstellt eine Variable\n- make Variablenname = Name/Wert\n
 - z.B. \n<make Wort = Baum\n<Wort\n
randomAnimal\n- wählt ein zufaelliges Tier aus unserer Liste aus\n- z.B.\n<randomAnimal
\nrandomAnimal Tiername1,Tiername2,Tiername3,...\n- wählt ein zufaelliges Tier
aus\n- du kannst selbst Tiernamen aus unserer Liste angeben\n- die Tiernamen müssen mit
einem Komma getrennt werden\n- z.B.\n<randomAnimal Tiger, Schwein, Huhn\n\nlistAnimals
- zeigt eine Liste unserer gewaehlten Tiere an\n\n"""