lista_slow = ["burak", "cukinia", "pomidor", "cytryna", "ananas", "papryka", "dynia"]
lista_temp = []

litera_uzyt = input("Podaj literą według, której chcesz filtrować: ")
for word in lista_slow:
    if litera_uzyt == word[0]:
        lista_temp.append(word)

print(f"Twoja lista to: {lista_temp}")
