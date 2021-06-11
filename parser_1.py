class Parser:
    def __init__(self):

        self._messages = []

    def parse(self, code):
        r = 0
        for zeile in code.split("\n"):
            if zeile.startswith("help") and len(zeile.rstrip()) < 5:
                self._messages.append(help_text)
            else:
                self._messages.append("Du hast den Befehl help falsch eingegeben. Versuche es nur mit 'help'.")
                return False
        return True


# gültig, aber darf nicht: help help
# "help"
# "help "
#
# ungültig, aber darf: help + enter, enter + help, help + space
# " help"
# "help
#  "
#

help_text = """say\n- fast gleiche Aufgabe wie print("") in Python 
- gibt einzelne Wörter aus\n- gibt folgende Zeichen wieder(a - z, A - Z, 0 - 9, alle
Zeichen außer Leerzeichen)\n- wenn ein Leerzeichen benutzt wird, werden alle
darauffolgenden Zeichen ignoriert\n- z.B.say Hallo09\n\nmake(=def)\n
randomAnimal\n- wählt ein zufaelliges Tier aus unserer Liste aus\n- z.B.randomAnimal
\nrandomAnimal Tiername1, Tiername2, Tiername3, ...\n- wählt ein zufaelliges Tier
aus\n- du kannst selbst Tiernamen aus unserer Liste angeben\n- die Tiernamen müssen mit
einem Komma getrennt werden\n- z.B.randomAnimal Tiger, Schwein, Huhn\n\nhelpAnimal
- zeigt eine Liste unserer gewaehlten Tiere an\n\n"""