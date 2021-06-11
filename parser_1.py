class Parser:
    def __init__(self):

        self._messages = []

    def parse(self, code):
        for zeile in code.split("\n"):


            if zeile.startswith("help") and len(zeile.rstrip()) < 5:
                self._messages.append(help_text)
            elif zeile.startswith("say "):
                said_text = zeile[3:len(zeile)]
                print(zeile)
                self._messages.append(said_text.lstrip())

            else:
                self._messages.append("Du hast mindestens einen Befehl falsch eingegeben. Versuche es mit 'help' für die Liste der Befehle.")
                return False
        return True

# darf:
# "say ..."
# "say ... ..."
# "say ... "
#
# darf nicht:
# " say ..."
# "say..."
# "say"
# "say "


help_text = """say\n- fast gleiche Aufgabe wie print("") in Python 
- gibt durch Leerzeichen zu trennende Wörter aus\n- gibt folgende Zeichen wieder(a - z, A - Z, 0 - 9, alle
 alle Zeichen)\n- wenn ein Leerzeichen benutzt wird, werden alle
darauffolgenden Zeichen ignoriert\n- z.B.say Hallo09\n\nmake(=def)\n
randomAnimal\n- wählt ein zufaelliges Tier aus unserer Liste aus\n- z.B.randomAnimal
\nrandomAnimal Tiername1, Tiername2, Tiername3, ...\n- wählt ein zufaelliges Tier
aus\n- du kannst selbst Tiernamen aus unserer Liste angeben\n- die Tiernamen müssen mit
einem Komma getrennt werden\n- z.B.randomAnimal Tiger, Schwein, Huhn\n\nhelpAnimal
- zeigt eine Liste unserer gewaehlten Tiere an\n\n"""