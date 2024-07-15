import json

def zapisz_dane_do_json(dane, sciezka_pliku):
    try:
        if not isinstance(dane, dict):
            raise ValueError("Dane muszą być w odpowiednim formacie (dict).")

        with open(sciezka_pliku, 'w', encoding='utf-8') as plik:
            json.dump(dane, plik, ensure_ascii=False, indent=4)
        print(f"Dane zostały zapisane do pliku {sciezka_pliku}")

    except ValueError as ve:
        print(f"Błąd wartości: {ve}")
    except FileNotFoundError:
        print(f"Nie znaleziono pliku lub katalogu {sciezka_pliku}.")
    except IOError as ioe:
        print(f"wejścia/wyjścia: {ioe}")
    except Exception as e:
        print(f"nieoczekiwany błąd: {e}")


if __name__ == "__main__":
    dane_poprawne = {
        "nazwa": "Przykład",
        "wartość": 123,
        "lista": [1, 2, 3, 4, 5],
        "slownik": {
            "klucz1": "wartość1",
            "klucz2": "wartość2"
        }
    }

    dane_bledne = ["nie", "jest", "to", "słownik"]

    sciezka_pliku = "dane.json"

    zapisz_dane_do_json(dane_poprawne, sciezka_pliku)
    zapisz_dane_do_json(dane_bledne, sciezka_pliku)
