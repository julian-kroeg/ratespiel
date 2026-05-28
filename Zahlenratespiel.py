
#Einstieg in die Zufallsfunktionen
import random

print("Willkommen zu meinem Ratespiel!")
print("Wer von Ihnen schafft es am schnellsten? :)")

#Aufbau des Schwierigkeitsgrades
print("Bitte wählen Sie einen Schwierigkeitsgrad aus:")
print("1 = entspannt (Eine Zahl zwischen 1 und 50)")
print("2 = anspruchsvoller (Eine Zahl zwischen 1 und 100)")
print("3 = anspruchsvoll (Eine Zahl zwischen 1 und 200)")

wahl = input("Ihre Wahl: ")

if wahl == "1":
    max_zahl = 50
elif wahl == "2":
    max_zahl = 100
elif wahl == "3":
    max_zahl = 200
else:
    print ("Ungültige Auswahl! Standard = anspruchsvoller")
    max_zahl = 100

zufalls_zahl = random.randint(1, max_zahl)

versuche = 0
erraten = False

input("Alles klar! Ich habe mir nun eine Zahl ausgedacht! Bitte drücken Sie Enter um zu starten!")

#Spielschleife mit Eingabesicherung
while not erraten:
    try:
        tipp= int(input("Bitte geben Sie ihren Tipp ab: "))
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein!")
        continue

    if tipp < 1 or tipp > max_zahl:
        print(f"Ungültiger Tipp! Bitte nur eine Zahl zwischen 1 und {max_zahl} eingeben!")
        continue

    versuche += 1

    if tipp < zufalls_zahl:
        print("Leider zu niedrig!")
    elif tipp > zufalls_zahl:
        print("Leider zu hoch!")
    else:
        print("Super! das ist die Richtige Zahl!")
        print(f"Sie haben {versuche} Versuche benötigt, um die richtige Zahl zu erraten!")
        erraten = True

input("Das Spiel ist beendet! Bitte drücken Sie Enter um das Programm zu schließen")