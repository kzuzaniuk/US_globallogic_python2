krotka = (10, -3, 4, 9, 12, -6, 0)
temp_liczba_min = krotka[0]
temp_liczba_max = krotka[0]

for i in range(len(krotka)):
    if krotka[i] > temp_liczba_max:
        temp_liczba_max = krotka[i]
        pass
    if krotka[i] < temp_liczba_min:
        temp_liczba_min = krotka[i]
        pass

print(f"Najmniejsza liczba to: {temp_liczba_min}")
print(f"Największa liczba to: {temp_liczba_max}")
