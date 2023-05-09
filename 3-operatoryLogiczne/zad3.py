wiek = int(input("Podaj ile masz lat: "))

if wiek >= 20:
    kat_a2 = True if input("Masz kategorię A2 co najmniej dwa lata? y/n: ") == 'y' else False
    # if (wiek >= 20 and kat_a2) or wiek >= 24:
    if kat_a2 or wiek >= 24:
        print("Możesz przystąpić do egzaminu na kat. A\n")
        pass
    else:
        print("Nie możesz przystąpić do egzaminu\n")
        pass
else:
    print("Nie możesz przystąpić do egzaminu\n")