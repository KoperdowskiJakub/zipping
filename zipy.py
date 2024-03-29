import zipfile
import datetime
import os

def sciezki(katalog): # zwraca sciezki do wszytskich plikow w wybvranym folderze
    sciezki = []
    for root, directories, files in os.walk(katalog): #iteruje przez wysztkie pliki i katalogi w podanym katalogu
        for nazwa_pliku in files:
            sciezka = os.path.join(root, nazwa_pliku)
            sciezki.append(sciezka)
    return sciezki# zwraca liste wszystkich plikow do kompresowania

def kompresowanie(sciezka):
    #lista sciezek wszystkich plikow w wybranym folderze
    pliki = sciezki(sciezka)
    #tworzy ze sciezki odpowiednia nazwe pliku z dzisiejsza data
    tmp = str(datetime.datetime.now())
    data = tmp.split()[0]
    lista = sciezka.split("/")
    nazwa = data
    nazwa += lista[-1]
    nazwa += ".zip"
    for plik in pliki:
        print(pliki)
    #zapisywanie skompresowanych plikow
    with zipfile.ZipFile(nazwa, "w") as zip:
        for plik in pliki:
            zip.write(plik)



