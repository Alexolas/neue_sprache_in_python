import random
class Parser:
    def __init__(self):

        self._messages = []

    def parse(self, code):
        list_animals = ['Alpaka', 'Elefant', 'Esel', 'Hase', 'Hund', 'Katze', 'Krokodil', 'Kuh', 'Löwe',
                        'Maus', 'Panda', 'Salamander', 'Schaf', 'Schwein', 'Tiger']
        variablen = {}
        for zeile in code.split("\n"):
            if zeile.startswith("help") and len(zeile.rstrip()) < 5:
                help_text = """say\n- fast gleiche Aufgabe wie print("") in Python 
                - gibt durch Leerzeichen zu trennende Wörter aus\n- gibt folgende Zeichen wieder(a - z, A - Z, 0 - 9, alle
                 alle Zeichen)\n- z.B.\n<say Hallo09\n\nmake\n- erstellt eine Variable\n- make Variablenname = Name/Wert\n
                 - z.B. \n<make Wort = Baum\n<$Wort\n
                randomAnimal\n- wählt ein zufaelliges Tier aus unserer Liste aus\n- z.B.\n<randomAnimal
                \nrandomAnimal Tiername1,Tiername2,Tiername3,...\n- wählt ein zufaelliges Tier
                aus\n- du kannst selbst Tiernamen aus unserer Liste angeben\n- die Tiernamen müssen mit
                einem Komma getrennt werden\n- z.B.\n<randomAnimal Tiger, Schwein, Huhn\n\nlistAnimals
                - zeigt eine Liste unserer gewaehlten Tiere an\nz.B.\n<listAnimals\n\n"""
                self._messages.append(help_text)
            elif zeile.startswith("say ") or zeile.startswith("s "):
                if zeile.startswith("s "):
                    said_text = zeile[1:len(zeile)].strip()
                else:
                    said_text = zeile[3:len(zeile)].strip()
                if said_text.startswith("$"):
                    var_name = said_text[1:len(said_text.strip())]
                    if var_name in variablen:
                        self._messages.append(variablen[var_name] + "\n")
                else:
                    self._messages.append(said_text.strip()+"\n")
            elif zeile.startswith("listanimals") or zeile.startswith("listAnimals") or zeile.startswith("la"):
                self._messages.append("Liste:")
                for l in list_animals:
                    self._messages.append("\n- " + l)
                self._messages.append("\n\n")
            elif zeile.startswith("randomAnimal") or zeile.startswith("randomanimal") or zeile.startswith("ra"):
                if len(zeile.rstrip()) == 12 or len(zeile.rstrip()) == 2:
                    self._messages.append(random.choice(list_animals))
                else:
                    if "," not in zeile:
                        self._messages.append("Die Tiernamen werden durch Kommata getrennt.")
                        return False
                    if zeile.startswith("randomAnimal"):
                        list = ''.join(zeile.split("randomAnimal "))
                    elif zeile.startswith("ra"):
                        list = ''.join(zeile.split("ra "))
                    else:
                        list = ''.join(zeile.split("randomanimal "))
                    for t in list.split(","):
                        if t.strip() not in list_animals:
                            self._messages.append("Ein oder mehrere Tiernamen existieren nicht. Wähle zwischen:\n- " + '\n- '.join(list_animals))
                            return False
                    e = random.choice(list.split(","))
                    self._messages.append(e.strip() + "\n")
            elif zeile.startswith("mk ") or zeile.startswith("make "):
                if zeile.startswith("mk") or zeile.startswith("mk "):
                    variable_und_wert = ''.join(zeile.split("mk "))
                else:
                    variable_und_wert = ''.join(zeile.split("make "))
                if "=" in zeile:
                    variable = variable_und_wert.split("=")[0].strip()
                    wert = variable_und_wert.split("=")[1].strip()
                    variablen[variable] = wert
                    self._messages.append("Variable '" + variable + "' mit dem Wert '" + wert + "' angenommen.\n")
                else:
                    return False
            elif zeile.startswith("$"):
                var_name = zeile[1:len(zeile.strip())]
                if var_name in variablen:
                    self._messages.append(variablen[var_name] + "\n")
                else:
                    self._messages.append("Diese Variable existiert nicht.\n")
            else:
                self._messages.append("Du hast wahrscheinlich einen Befehl falsch eingegeben. Versuche es mit 'help' für die Liste der Befehle.\n")
                return False
        return True
