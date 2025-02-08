def zamienNaAscii(line):
    suma = 0
    for litera in list(line):
        suma += ord(litera)
    return suma

def czyPierwsza(number):
    for i in range (2, number):
        if number % i == 0:
            return False
    return True

def czyAsciiRosnie(line):
    temp = line[0]
    for litera in line[1:]:
        if ord(litera) <= ord(temp):
            return False
        temp = litera
    return True

lista_slow = []
def czyJuzWystepowal(line):
    if line in lista_slow:
        return True
    lista_slow.append(line)
    return False

with open("../dane_PR/NAPIS.TXT", "r") as file:
    line = file.readline().strip()

    iloscPierwszych = 0
    napisyRosnace = []
    duplikaty = []
    while line != "":
        ascii = zamienNaAscii(line)
        if czyPierwsza(ascii) == True:
            iloscPierwszych += 1

        if czyAsciiRosnie(line) == True:
            napisyRosnace.append(line)

        if czyJuzWystepowal(line) == True:
            duplikaty.append(line)

        line = file.readline().strip()
    print("W pliku znajduje się", iloscPierwszych, "liczb pierwszych.")
    print("Napisy rosnace:", napisyRosnace)
    print("Duplikaty:", duplikaty)