import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

def generatorDanychZOdchyleniem():  # Funkcja generujaca dane losowe z uwzglednieniem odchylenia standardowego
        mu = 30.0  # liczba podstawowa
        sigma = 3.0 # odchylenie standardowe
        data = np.array(np.random.randn(1000) * sigma + mu)
        data = data.astype(int)
        #hx, hy, _ = plt.hist(data[0], bins=50)
        #plt.show()
        data.tolist()  # zamiana typu danych w liste
        for i in range(len(data)):  # Zabezpieczenie w przypadku, jesli wygeneruje sie liczba mniejsza od 0
                if data[i] < 0:
                        data[i] = abs(data[i])
        print(data)
        return data

def generatorDanychLosowychZZerem():  # Funkcja generujaca dane losowe z zerem
        data = np.random.randint(0,100,1000) # losowanie liczb z zakresu od 0 do 100, 3 zmienna mowi o ilosci liczb
        data = data.tolist()  # zamiana typu danych w liste
        return data

def generatorDanychLosowychBezZera():  # Funkcja generujaca dane losowe bez zera
        data = np.random.randint(1,100,1000) # losowanie liczb z zakresu od 0 do 100, 3 zmienna mowi o ilosci liczb
        data = data.tolist()  # Zamiana typu danych w liste
        return data



