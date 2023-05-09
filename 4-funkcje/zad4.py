def dodawanie(liczba1: float, liczba2: float) -> None:
    """Funkcja dodaje dwie liczby typu float i wyświetla wynik"""
    print(f"{liczba1} + {liczba2} = {liczba1+liczba2}\n")

def odejmowanie(liczba1: float, liczba2: float) -> None:
    """Funkcja odejmuje dwie liczby typu float i wyświetla wynik"""
    print(f"{liczba1} - {liczba2} = {liczba1-liczba2}\n")

def mnozenie(liczba1: float, liczba2: float) -> None:
    """Funkcja mnoży dwie liczby typu float i wyświetla wynik"""
    print(f"{liczba1} x {liczba2} = {liczba1*liczba2}\n")

def dzielenie(liczba1: float, liczba2: float) -> None:
    """Funkcja dzieli jedną liczbę typu float przez drugą i wyświetla wynik"""
    if liczba2 == 0:
        print("Nie dzielimy przez 0\n")
    else:
        print(f"{liczba1} / {liczba2} = {liczba1/liczba2}\n")
  
    
def kalkulator(operacja: int, liczba1: float, liczba2: float) -> None:
    """Główna funkcja kalkulatora, przyjmuje, jako argument rodzaj operacji i wywołuje odpowiednią podfunkcję kalkulatora"""
    if operacja == 1:
        dodawanie(liczba1, liczba2)
    elif operacja == 2:
        odejmowanie(liczba1, liczba2)
    elif operacja == 3:
        mnozenie(liczba1, liczba2)
    elif operacja == 4:
        dzielenie(liczba1, liczba2)

    
def print_info() -> None:
    """Funkcja odpowiedzialna za wyświetlenie informacji - dostępnych funkcji kalkulatora"""
    print("""Dostępne funkcje to:
          \n1. Dodawanie
          \n2. Odejmowanie
          \n3. Mnożenie
          \n4. Dzielenie
          \n0. Wyjdź
          """)

def get_user_choice() -> int:
    """Funkcja, która pobiera od użytkownika liczbę (numer wybranej podfunkcji kalkulatora) i zwraca ją w miejscu wywołania"""
    return int(input("Wybierz operację za pomocą odpowiedniej liczby: "))

def pobierz_liczby() -> tuple:
    """Funkcja pobiera dwie liczby i zwraca je, jako tuple do rozpakowania"""
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Pojda drugą liczbę: "))
    return liczba1, liczba2

def main() -> None:
    """Główna pętla kalkulatora"""
    while True:
        print_info()
        operacja = get_user_choice()
        if operacja == 0:
            return
        else:
            liczba1, liczba2 = pobierz_liczby()
            kalkulator(operacja, liczba1, liczba2)
            
main()