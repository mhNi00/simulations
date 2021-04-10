def SJF(burst_time, arrival_time):  # Funkcja wykonujaca symulace procesora z wykorzystaniem algorytmu SJF
    new_burst_time = []
    takt = 0  # takty procesora, jedna iteracja w petli to jeden takt ( W uproszczeniu )
    kolejka_procesow = []
    licznik = 0
    if 0 not in arrival_time:  # Uwzglednienie sytuacji, w ktorej na poczatku nie ma zadnych procesow
        takt = takt + min(arrival_time)
    while True:
        for i in range(len(arrival_time)):
            if takt == arrival_time[i]:  # Dodawanie procesow do kolejki, jezeli takt jest rowny czasowi przyjscia
                kolejka_procesow.append(i)
                new_burst_time.append(burst_time[i])
                for j in range(len(kolejka_procesow)):  # Ta czesc kodu wykonuje zamiane procesow wzgledem czasu trwania procesow
                    if new_burst_time[j] != burst_time[kolejka_procesow[j]]:
                        licznik = licznik + 1
                if len(kolejka_procesow) - licznik >= 2:
                    for k in range(licznik,
                                   len(kolejka_procesow)):
                        for l in range(licznik, len(kolejka_procesow) - 1):
                            if new_burst_time[l] > new_burst_time[l + 1]:
                                kolejka_procesow[l], kolejka_procesow[l + 1] = kolejka_procesow[l + 1], \
                                                                               kolejka_procesow[l]
                                new_burst_time[l], new_burst_time[l + 1] = new_burst_time[l + 1], new_burst_time[l]

                licznik = 0
        for i in range(len(new_burst_time)):
            if new_burst_time[i] != 0:
                new_burst_time[i]=new_burst_time[i] - 1  # Zmniejszenie czasu wykonywania procesu o 1
                break
        #if new_burst_time[0] == 0:
        #    new_burst_time.append(
        #        new_burst_time.pop(new_burst_time.index(new_burst_time[0])))  # WYRZUCAM ZAKONCZONY PROCES NA KONIEC
        #    popper = popper + 1
        #if new_burst_time[0] > 0:
        #    new_burst_time[0] = new_burst_time[0] - 1  # ZMNIEJSZAM CZAS WYKONYWANIA PROCESU O 1
        if len(kolejka_procesow) == len(arrival_time):
            if new_burst_time.count(new_burst_time[0]) == len(
                    new_burst_time):  # Jesli wszystkie procesy sa rowne 0 symulacja jest zakonczona
                return kolejka_procesow
        takt = takt + 1