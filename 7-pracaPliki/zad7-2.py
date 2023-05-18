# from itertools import combinations, product - opcja do przemyślenia
from os import path
import random

file1_name = 'imiona.txt'
file2_name = 'nazwiska.txt'
current_dir = path.dirname(__file__)

def pobierz_liczbe():
    return int(input("Podaj liczbę kombinacji do wylosowania: "))

def generate_unique_names() -> None:
    with open(path.join(current_dir, file1_name), 'r', encoding='utf-8') as f1, \
        open(path.join(current_dir, file2_name), 'r', encoding='utf-8') as f2:
            imiona_list = f1.readlines()
            imiona_list = [x.rstrip('\n') for x in imiona_list]
            nazwiska_list = f2.readlines()
            nazwiska_list = [x.rstrip('\n') for x in nazwiska_list]
            generated: set[str] = set() #set gwarantuje unikalne elementy
            liczba = pobierz_liczbe()
            while len(generated) < liczba:
                generated.add(random.choice(imiona_list) + ' ' + random.choice(nazwiska_list))
            print(generated)
            
generate_unique_names()