
def MFU(strony):  # Funkcja wykonujaca symulace zamiany stron z wykorzystaniem algorytmu FIFO
    f = open("danedlaMFU.txt", "a")  # Otwarcie pliku tekstowego
    licznik_podmiany_stron = 0 # ile razy podmienia sie strony
    lista_liczby_odwolan = [0] * 101 # ile razy odwolanie pojawilo sie, tablica ma 100 miejsc poniewaz generowane sa liczby do 100 maks.
    czasy_zaladowania_strony = [] # do sredniej
    lista_ramek = [0] * 5 # ustalanie ilosc ramek na 5
    czas_w_ramce = [0] * 5 # jak dlugo strona jest zaladowana w buforze
    i = 0
    dodatkowy_licznik = 0
    while True:
        if i == len(strony):  # Gdy iteracja dojdzie do ilosci wszystkich stron program zostaje zakonczony
            break
        for j in range(len(lista_ramek)):  # Jezeli w ramce jest jakas strona to jej czas w ramce zostaje zwiekszony o 1
            if lista_ramek[j] != 0:
                czas_w_ramce[j] = czas_w_ramce[j] + 1
        if 0 in lista_ramek:
            if strony[i] not in lista_ramek: # Wypelnianie listy ramek dopoki sa puste miesjca
                lista_ramek[i - dodatkowy_licznik] = strony[i]
            else:
                dodatkowy_licznik = dodatkowy_licznik + 1
        if 0 not in lista_ramek:  # Lista jest zapelniona, nalezy skorzystac z algorytmu MFU
            if strony[i] not in lista_ramek:  # Jezeli strony nie ma w liscie ramek korzystamy z MFU
                kandydat = max (lista_liczby_odwolan)  # Kandydatem do podmiany jest liczba o najwiekszej liczbie odwolan
                for j in range(len(lista_liczby_odwolan)):  # Wyszukiwanie indexu kandydata w liscie liczby odwolan
                    if lista_liczby_odwolan[j] == kandydat:
                        index_kandydata_do_podmiany = j
                        break
                miejsce = lista_ramek.index(index_kandydata_do_podmiany)  # zmienna przechowujaca miejsce kandydata w liscie ramek
                czasy_zaladowania_strony.append(lista_ramek[miejsce]) # dodaje czasy w buforze do sredniej
                czas_w_ramce[miejsce] = 0  # zerowanie i podmienianie wybranych zmiennych
                lista_ramek[miejsce] = strony[i]
                licznik_podmiany_stron = licznik_podmiany_stron + 1
                lista_liczby_odwolan[index_kandydata_do_podmiany] = 0
        lista_liczby_odwolan[strony[i]] = lista_liczby_odwolan[strony[i]] + 1  # zwiekszenie liczby odwolan strony o 1
        i = i + 1
        #print("lista_ramek: ", lista_ramek, "------------")  # wizualizacje procesu
        #print("lista liczby odwolan: ", lista_liczby_odwolan)
        #print("kolejka: ", strony)
        #print(" TAKT: ", i)
    #print("Ile razy podmieniono strone: ", licznik_podmiany_stron)
    #print("Sredni czas strony w buforze: ", sum(czas_w_ramce)/len(czas_w_ramce))
    f.write(str(licznik_podmiany_stron))  # Zapisywanie danych do pliku
    f.write(" ")
    f.write(str(sum(czas_w_ramce)/len(czas_w_ramce)))
    f.write("\n")
    f.close()