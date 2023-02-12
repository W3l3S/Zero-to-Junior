import random

print("----------GRA PAPIER, KAMIEN, NOZYCZKI----------")

def poczatek():
    gra=int(input("Gra z komputerem - wpisz 1.\nGra z drugim człowiekiem - wpisz 2.\nWyjscie 3.\n"))

    while int(gra)<0 or int(gra)>3:
        print("Podales/as zla cyfre. Wpisz poprawna cyfre.")
        gra = input("")

    if gra==1:
        komputer()
    elif gra==2:
        czlowiek()
    else:
        print("Dziekuje za gre :D")

def komputer():
    print("-----Gra z komputerem-----")
    komp=random.choice(["papier","kamien","nozyczki"])
    print("Wybierz: 'papier','kamien','nozyczki'")
    przeciwnik=input()
    print(f"Komputer wybrał: {komp}\nCzlowiek wybrał: {przeciwnik}")
    print(wynik(komp, przeciwnik))

    poczatek()

def czlowiek():
    print("-----Gra z drugim człowiekiem-----\nPierwszy przeciwnik wybiera: 'papier','kamien','nozyczki'")
    przeciwnik = input()
    print("Drugi przeciwnik wybiera: 'papier','kamien','nozyczki'")
    przeciwnik2 = input()
    print(f"Pierwszy przeciwnik wybrał: {przeciwnik}\nDrugi przeciwnik wybrał: {przeciwnik2}")
    print(wynik(przeciwnik, przeciwnik2))

    poczatek()

def wynik(x,y):
    if x=="papier" and y=="kamien" or x=="kamien" and y=="papier":
        print("Papier jest silniejszy od kamienia, poniewaz go owija. Wygrywa papier.")
    elif x=="kamien" and y=="nozyczki" or x=="nozyczki" and y=="kamien":
        print("Kamien jest silniejszy od nozyczek, poniewaz je tep. Wygrywa kamien.")
    elif x=="papier" and y=="nozyczki" or x=="nozyczki" and y=="papier" :
        print("Nozyczki sa silniejsze od papieru, poniewaz go tna. Wygrywaja nozyczki.")
    else:
        print("Remis.")

poczatek()