import random

liczba_strzalow = 0
liczba_losowa = random.randint(0, 100)
liczba_uzyt = 0

while True:
    liczba_uzyt = int(input("Zgadnij liczbę z przedziału 0-100: "))
    liczba_strzalow += 1
    if liczba_uzyt < liczba_losowa:
        print("Podana przez Ciebie liczba jest zbyt mała\n")
        continue
    elif liczba_uzyt > liczba_losowa:
        print("Podana przez Ciebie liczba jest zbyt duża\n")
        continue
    elif liczba_uzyt == liczba_losowa:
        print(f"Dobra robota, zgadłeś za {liczba_strzalow} razem!")
        # still_going = False
        if input("Chcesz zagrać jeszcze raz? Odpowiedz y/n ") == 'y':
            liczba_losowa = random.randint(0, 100)
            liczba_strzalow = 0
            continue
        else:
            print("Koniec gry")
            break
    