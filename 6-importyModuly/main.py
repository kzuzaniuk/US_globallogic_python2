from mod1 import print_info, get_user_choice, pobierz_liczby, kalkulator

def main() -> None:
    """Główna pętla kalkulatora"""
    while True:
        print_info()
        operacja = get_user_choice()
        if operacja == 0:
            break
        else:
            liczba1, liczba2 = pobierz_liczby()
            kalkulator(operacja, liczba1, liczba2)
            
main()