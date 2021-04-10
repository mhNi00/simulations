def FIFO(strony): # Funkcja wykonujaca symulace zamiany stron z wykorzystaniem algorytmu FIFO
    f = open("danedlaFIFO.txt", "a")  # Otwarcie pliku tekstowego
    licznik_podmiany_stron = 0 # ile razy podmienia sie strony
    czasy_zaladowania_strony = [] # do sredniej
    lista_ramek = [0] * 5 # ustalanie ilosc ramek na 5
    czas_w_ramce = [0] * 5 # jak dlugo strona jest zaladowana w buforze
    i = 0
    dodatkowy_licznik = 0
    while True:  # Petla glowna programu
        if i == len(strony): # Jezeli iteracja petli dojdzie do ilosci stron program zostaje zakonczony
            break
        for j in range(len(lista_ramek)):  # Jezeli w ramce jest jakas strona to jej czas w ramce zostaje zwiekszony o 1
            if lista_ramek[j] != 0:
                czas_w_ramce[j] = czas_w_ramce[j] + 1
        if 0 in lista_ramek:
            if strony[i] not in lista_ramek: # Wypelnianie listy ramek dopoki sa puste miesjca
                lista_ramek[i - dodatkowy_licznik] = strony[i]
            else:
                dodatkowy_licznik = dodatkowy_licznik + 1
        if 0 not in lista_ramek:  # lista ramek jest zapelniona, trzeba skorzystac z algorytmu FIFO
            if strony[i] not in lista_ramek:  # jezeli strony brakuje w liscie ramek trzeba dokonac podmiany
                max_czas_w_ramce = max(czas_w_ramce)  # kandydatem jest strona o najdluzszym casie w ramce
                index_max_czasu_w_ramce = czas_w_ramce.index(max_czas_w_ramce)
                czasy_zaladowania_strony.append(lista_ramek[index_max_czasu_w_ramce]) # dodanie czasu w buforze do sredniej
                czas_w_ramce[index_max_czasu_w_ramce] = 0  # Zerowanie czasu w ramce po podmianie procesu
                lista_ramek[index_max_czasu_w_ramce] = strony[i] # Nastepuje podmiana
                licznik_podmiany_stron = licznik_podmiany_stron + 1 # Zwiekszanie ilosci podmiany stron o 1
        i = i + 1

        #print("lista_ramek: ", lista_ramek, "------------")  # wizualizacja procesu
        #print("czasy w ramce: ", czas_w_ramce)
        #print("kolejka: ", strony)
    #print("Ile razy podmieniono strone: ", licznik_podmiany_stron)
    #print("Sredni czas strony w buforze: ", sum(czas_w_ramce)/len(czas_w_ramce))
    f.write(str(licznik_podmiany_stron))  # Zapisanie danych do pliku tekstowego
    f.write(" ")
    f.write(str(sum(czas_w_ramce) / len(czas_w_ramce)))
    f.write("\n")
    f.close()


