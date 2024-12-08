
__author__ = "7592047, Khauto"
__email__ = "khauto@em.uni-frankfurt.de"


"""
Aufgabe 1)

a)
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            print(f"{i} * {j} * {k} = {i * j * k}")

Dieser Code berechnet das Produkt von i, j und k für alle Werte in range(1, 4). 
Da jeder range(1, 4) nur die Werte 1, 2 und 3 enthält, werden alle Kombinationen dieser Werte ausgegeben.

Ausgabe:
1 * 1 * 1 = 1
1 * 1 * 2 = 2
1 * 1 * 3 = 3
1 * 2 * 1 = 2
1 * 2 * 2 = 4
1 * 2 * 3 = 6
1 * 3 * 1 = 3
1 * 3 * 2 = 6
1 * 3 * 3 = 9
2 * 1 * 1 = 2
2 * 1 * 2 = 4
2 * 1 * 3 = 6
2 * 2 * 1 = 4
2 * 2 * 2 = 8
2 * 2 * 3 = 12
2 * 3 * 1 = 6
2 * 3 * 2 = 12
2 * 3 * 3 = 18
3 * 1 * 1 = 3
3 * 1 * 2 = 6
3 * 1 * 3 = 9
3 * 2 * 1 = 6
3 * 2 * 2 = 12
3 * 2 * 3 = 18
3 * 3 * 1 = 9
3 * 3 * 2 = 18
3 * 3 * 3 = 27


b)
count = 3
while count > 0:
    for j in range(count):
        print("Countdown:", count, "-", j)
    count -= 1

Dieser Code verwendet eine while-Schleife, die ab count = 3 startet und jedes Mal um 1 reduziert wird, 
bis count == 0. Innerhalb der while-Schleife läuft eine for-Schleife von 0 bis count - 1, was für jeden 
count-Wert eine neue Ausgabe erzeugt.

Ausgabe:

Countdown: 3 - 0
Countdown: 3 - 1
Countdown: 3 - 2
Countdown: 2 - 0
Countdown: 2 - 1
Countdown: 1 - 0


c)
counter = 1
while counter <= 5:
    counter += 1
    print(counter)

Dieser Code erhöht den Wert von counter um 1 und gibt ihn dann aus, solange counter <= 5 ist. 
Da counter bereits vor der Ausgabe erhöht wird, beginnt die Ausgabe bei 2 und endet bei 6.

Ausgabe:
2
3
4
5
6


d)
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

In diesem Code wird counter zunächst ausgegeben und dann erhöht. 
Die Schleife läuft solange counter <= 5 ist, sodass counter von 1 bis 5 ausgegeben wird.

Ausgabe:
1
2
3
4
5


"""