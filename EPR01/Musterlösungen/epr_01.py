"""
    Die Lösungen sind für Anfänger gedacht und müssen nicht komplex sein!

    Die Struktuierung in Funktionen ist für dieses Aufgabenblatt kein Muss, es kann also
    jede Aufgabe separat in einem eigenen Modul gelöst werden.
    Hier dient es nur um verschiedene Module zu sparen.

    Alles was mit Coding zu tun hat, wie Kommentare, Variablennamen, Docstrings usw.. 
    sollten auf Englisch sein und hier sind
    nur die Hinweise auf Deutsch. Das sollte für das jetzige Blatt noch nicht bewertet werden
    (korrigeren mit Hinweisen für die Zukunft aber ja), sollte aber in den zukünftigen Blättern.

    Die dritte Aufgabe kann natürlich auf Deutsch bleiben.
"""

__author__ = "7592047, Khauto"
__email__ = "khauto@em.uni-frankfurt.de"

def exer1():
    """Celsius to Fahrenheit calculator"""

    # input
    cel = float(input("Gib die Temperatur in Celsius ein: "))

    # calculation
    fahr = cel * (9/5) + 32

    # output
    print(f"Die Temperatur in Fahrenheit betraegt: {fahr}")


def exer2():
    """Supermarket calculator"""

    # inputs
    price = float(input("Gib den Preis pro Produkt ein: "))
    number = int(input("Gib die Anzahl der Pridukte ein: "))

    discount = 0.0

    # discount logic
    if number >= 100:
        discount = 0.15
    elif number >= 10:
        discount = 0.07
    elif number >= 5:
        discount = 0.05

    # calculation
    total = price * number
    total -= (total * discount)

    # outputs
    if discount == 0:
        print("Du bekommst keinen Rabatt!")
    else:
        print(f"Du bekommst {int(discount * 100)}% Rabatt.")

    print(f"Der Gesamtpreis ist {total:.2f}")


"""
Aufgabe 3:

Wichtig hier ist, dass nicht unbedingt die genaue Fehlerklasse wie von python defniert genannt zu werden, sondern reicht es
jetzt einfach den Fehler zu finden und erklären warum.
Die Erklärung hat mehr Gewicht als einfach den falschen Code laufen zu lassen und einfach copy paste.


a)
Frage:

name = input("Wie ist dein Name? ") 
print("Hallo, " + Name + "! Willkommen.")

(name != Name)

lösung:

name = input("Wie ist dein Name? ") 
print("Hallo, " + name + "! Willkommen.")


b)
Frage:

radius = input("Gib den Radius des Kreises ein: ")
circumference = 2 * 3.14 * radius
print("Der Umfang des Kreises beträgt: " + circumference)

Fehler1: radius ist string, kann mit int oder float nicht multipliziert werden
Fehler2: circumference sollte float sein wenn radius richtig ist, und somit kann mit string im print-Statement nicht addiert werden.

Lösung:

radius = float(input("Gib den Radius des Kreises ein: "))
circumference = 2 * 3.14 * radius
print("Der Umfang des Kreises beträgt: " + str(circumference)) ## or print(f"Der Umfang des Kreises beträgt: {circumference}")


c)
Frage:

num = input("Gib eine Zahl ein: ")
if num = 0: print("Die Zahl ist null.")         
elif num < 0: print("Die Zahl ist negativ.")     
else: print("Die Zahl ist positiv.")

1- num ist string
2- num == 0: und nicht num = 0

Lösung:

num = eval(input("Gib eine Zahl ein: ")) # or int(input("Gib eine Zahl ein: ")) depending on the user's preference
if num == 0: print("Die Zahl ist null.")
elif num < 0: print("Die Zahl ist negativ.")
else: print("Die Zahl ist positiv.")

d)
Frage:

a = 5
b = 10
if b:
print("b gibt True")
else:
print("b gibt False")

Die Einrückungen fehlen, wenn es in eine neue Zeile geschrieben wird.

Lösung:

a = 5
b = 10
if b:
    print("b gibt True")
else:
    print("b gibt False")

oder

a = 5
b = 10
if b: print("b gibt True")
else: print("b gibt False")

"""

def main():
    """driver function"""

    exer1()
    exer2()


if __name__ == "__main__":
    main()
