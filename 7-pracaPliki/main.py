from os import path
import re
import string

alphabet = dict.fromkeys(list(string.ascii_lowercase), 0) #dict dla poszczególnych liter
# print(alphabet)

data_name = 'tekst.txt'
current_dir = path.dirname(__file__)
data_path = path.join(current_dir, data_name)

d = ";,.\n "
reg_exp = "["+"\\".join(d)+"]"

#https://stackoverflow.com/questions/35221535/python-removing-delimiters-from-strings
#ogarnąć regexy bardziej, przydatne

def word_counter() -> None:
    with open(data_path, 'r', encoding='utf-8') as f:
        whole_text = f.read()
        clean_text = re.split(reg_exp, whole_text) 
        clean_text = [x for x in clean_text if x]
        
        # print(clean_text) #wyczyszczony tekst z seperatorów i innych dziwnych znaków
        print("Liczba słów:", len(clean_text))
        
        for w in clean_text:
            alphabet[w[-1]] += 1
            
        print("Statystyki (na jakie litery kończą się słowa): \n", alphabet)
        
        
word_counter()

#318 słów
