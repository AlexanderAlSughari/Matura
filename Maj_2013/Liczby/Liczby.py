def czyRownaOstatniej(number):
    if number[:1] == number[len(number)-1:]:
        return True
    return False

def czyLiczbaZnaczaca(number):
    for i in range(0, len(number)-1):
        if number[i] > number[i+1]:
            return False
    return True

with open("../Dane/dane.txt","r") as file:
    line = file.readline().strip()

    rowne1 = 0
    rowne2 = 0
    znaczace = []
    while line != "":
        if czyRownaOstatniej(line) == True:
            rowne1 += 1

        if czyRownaOstatniej(str(int(line, 8))) == True:
            rowne2 += 1

        if czyLiczbaZnaczaca(line) == True:
            znaczace.append(line)

        line = file.readline().strip()
    print("W pliku jest", rowne1, "liczb, które mają taką samą pierwszą i ostatnią cyfrę")
    print("W pliku jest", rowne2, "liczb dziesietnych, które mają taką samą pierwszą i ostatnią cyfrę")
    print("Suma liczby znaczacych:", len(znaczace), "| [min:", min(map(int, znaczace)),"] max[:", max(map(int, znaczace)),"]")