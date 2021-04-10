import genDanych
import symulacja_procesora_FCFS
import symulacja_procesora_SJF
import alg_zastepowania_stron_FIFO
import alg_zastepowania_stron_MFU
import copy


def znajdzCzasOczekiwania(n, bt, wt, at):  # Funkcja do obliczenia czasu oczekiwania
    service_time = [0] * n
    service_time[0] = 0
    wt[0] = 0
    for i in range(1, n):  # petla do obliczania czasu oczekiwania
        service_time[i] = (service_time[i - 1] + bt[i - 1])  # Dodaje czas trwania poprzedniego procesu
        wt[i] = service_time[i] - at[i]  # Obliczanie czasu oczekiwania dla procesu
        if wt[i] < 0:  # Jezeli czas czekania dla procesu jest mniejszy od 0 tzn ze jest gotowy
            wt[i] = 0


def znajdzCzasRealizacji(n, bt, wt, tat):  # Funkcja do obliczania czasu realizacji
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def znajdzSredniCzas(n, bt, at):  # Funkcja do liczenia sredniego czasu oczekiwania i realizacji procesow
    wt = [0] * n
    tat = [0] * n
    znajdzCzasOczekiwania(n, bt, wt, at)  # Funkcja do obliczenia czasu oczekiwania procesow
    znajdzCzasRealizacji(n, bt, wt, tat)  # Funkcja do obliczenia czasu realizacji
    print("Processes|Burst Time|Arrival Time|Waiting Time|Turn-Around Time|Completion Time \n")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time = tat[i] + at[i]
        print(" ", i + 1, "         ", bt[i], "         ", at[i], "          ", wt[i], "         ", tat[i], "        ",
              compl_time)
    print("Average waiting time = %.5f " % (total_wt / n))
    print("\nAverage turn around time = ", total_tat / n)
    f2.write(str(total_wt/n))
    f2.write(" ")
    f2.write(str(total_tat/n))
    f2.write("\n")


if __name__ == "__main__":
    f = open("wygenerowanedane.txt", "a")  # Operacje z plikami tekstowymi
    f2 = open("danedoobliczenproc.txt", "a")
    f2.write("waitingtime turnaroundtime")
    f2.write("\n")
    f.write("Dane testowe dla algorytmow czasu procesora\n")
    for i in range(10):   # Powtorzanie metody 10 razy aby miec wiecej danych
        n = 10  # Ilosc procesow
        burst_time = [1,2,3,4,5,3,2,1,8,10]  # Czas trwania wszystkich procesow
        print(burst_time)
        arrival_time = [1,2,3,4,8,6,3,2,1,2]  # Czas nadejscia wszystkich procesow
        f.write(str(i))  # Zapisywanie do plikow tekstowych
        f.write("\n")
        f.write("Burst time: ")
        f.write(str(burst_time))
        f.write("\n")
        f.write("Arrival_time: ")
        f.write(str(arrival_time))
        f.write("\n")
        new_burst_time = []  # Listy, ktore sa wykorzystywane w pozniejszych obliczeniach srednich czasow trwania
        new_arrival_time = []
        new_burst_time_1 = []
        new_arrival_time_1 = []
        processes = symulacja_procesora_FCFS.FCFS(copy.deepcopy(burst_time), arrival_time)  # Inicjalizacja symulacji FCFS
        print("Zakonczono symulacje procesora z wykorzystaniem FCFS")
        processes2 = symulacja_procesora_SJF.SJF(copy.deepcopy(burst_time), arrival_time)  # Inicjalizacja symulacji SJF
        print("Zakonczono symulacje procesora z wykorzystaniem SJF")
        print("Kolejka wykonywania procesow z wykorzestaniem FCFS: ", processes)
        print("Kolejka wykonywania procesow z wykorzystaniem SJF: ", processes2)
        for i in range(len(processes)):  # Uzupelnianie czasow wedlug kolejki w celu wykonania obliczen srednich
            new_burst_time.append(burst_time[processes[i]])
            new_arrival_time.append((arrival_time[processes[i]]))
            new_burst_time_1.append(burst_time[processes2[i]])
            new_arrival_time_1.append(arrival_time[processes2[i]])
        for i in range(len(processes)):  # Podbijanie indeksow procesow aby liczenie zaczynalo sie od jedynki
            processes[i] = processes[i] + 1
            processes2[i] = processes2[i] + 1
        print(new_burst_time)
        print(new_arrival_time)
        print("-----------------ZESTAWIENIE DLA FCFS---------------------")
        znajdzSredniCzas(n, new_burst_time, new_arrival_time)
        print("-----------------ZESTAWIENIE DLA SJF----------------------")
        znajdzSredniCzas(n, new_burst_time_1, new_arrival_time_1)
    print("-----------------ZASTEPOWANIE STRON-----------------------")
    f.write("Dane testowe dla algorytmu zastepowania stron\n")
    for i in range(10):  # Powtarzanie metody 10 razy aby miec wiecej danych
        strony = [1,2,3,4,5,6,7,8,9,10]
        # Lista ze stronami
        f.write(str(i))  # Zapisywanie danych do pliku tekstowego
        f.write("\n")
        f.write("Lista odwolan: ")
        f.write(str(strony))
        f.write("\n")
        print("-----------------ZESTAWIENIE DLA FIFO---------------------")
        alg_zastepowania_stron_FIFO.FIFO(strony)  # Inicjalizacja symulacji algorytmu FIFO
        print("-----------------ZESTAWIENIE DLA MFU----------------------")
        alg_zastepowania_stron_MFU.MFU(strony)  # Inicjalizacja symulacji algorytmu MFU
    f2.close()  # Zamkniecie plikow tekstowych
    f.close()

# Do utworzenia funkcji obliczajacych czasy srednie wykorzystano pomoc ze strony internetowej
# https://www.geeksforgeeks.org/program-for-fcfs-cpu-scheduling-set-2-processes-with-different-arrival-times/

