import json
import os

def wczytaj_json(plik_json):

    if not os.path.isfile(plik_json):
        print(f"Plik {plik_json} nie istnieje.")
        return None

    try:
        with open(plik_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print("Poprawnie wczytano dane z pliku JSON")
            return data
    except FileNotFoundError:
        print(f"Plik {plik_json} nie został znaleziony.")
    except json.JSONDecodeError as e:
        print(f"Błąd dekodowania pliku JSON: {e}")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")
    return None

def waliduj_dane(data):
    if not isinstance(data, dict):
        print("Dane w pliku JSON nie są w poprawnym słowniku")
        return False

    wymagane_klucze = ["klucz1", "klucz2"]  # Zmień na odpowiednie klucze
    for klucz in wymagane_klucze:
        if klucz not in data:
            print(f"Brakujący klucz w danych JSON: {klucz}")
            return False

    return True

def main():
    plik_json = 'plik.json'
    dane = wczytaj_json(plik_json)
    
    if dane is not None:
        if waliduj_dane(dane):
            print("Dane są poprawne i można je użyć")
        else:
            print("dane nie są poprawne.")
    else:
        print("Nie udało się wczytać danych.")

if __name__ == "__main__":
    main()
