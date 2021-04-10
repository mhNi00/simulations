def FCFS(burst_time, arrival_time):  # Funkcja wykonujaca symulace procesora z wykorzystaniem algorytmu SJF
    new_burst_time = []
    takt = 0  # takty procesora, jedna iteracja petli to jeden takt ( w uproszczeniu )
    kolejka_procesow = []
    if 0 not in arrival_time:  # Uwzglednienie sytuacji, w ktorej na poczatku nie ma zadnych procesow
        takt = takt + min(arrival_time)
    while True:  # Petla glowna symulacji
        for i in range(len(arrival_time)):
            if takt == arrival_time[i]:  # Dodawanie procesow do kolejki, jezeli takt jest rowny czasowi przyjscia
                kolejka_procesow.append(i)
                new_burst_time.append(burst_time[i])

        if new_burst_time[0] == 0:
            new_burst_time.append(
                new_burst_time.pop(new_burst_time.index(new_burst_time[0])))  # Wyrzucanie zakonczonego procesu na koniec
        if new_burst_time[0] > 0:
            new_burst_time[0] = new_burst_time[0] - 1  # Zmniejszenie czasu wykonywania procesu o 1
        if len(kolejka_procesow) == len(arrival_time):
            if new_burst_time.count(new_burst_time[0]) == len(
                    new_burst_time):  # Jesli wszystkie procesy sa rowne 0 symulacja jest zakonczona
                return kolejka_procesow
        takt = takt + 1