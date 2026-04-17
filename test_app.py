from app import dodaj, odejmij, pomnoz, podziel

def test_dodaj():
    assert dodaj(2, 3) == 5
    assert dodaj(-1, 1) == 0

def test_odejmij():
    assert odejmij(10, 4) == 6
    assert odejmij(0, 5) == -5

def test_pomnoz():
    assert pomnoz(3, 5) == 15
    assert pomnoz(0, 99) == 0

def test_podziel():
    assert podziel(10, 2) == 5
    assert podziel(0, 5) == 0
    assert podziel(7, 0) == "Blad: dzielenie przez zero"

if __name__ == "__main__":
    test_dodaj()
    test_odejmij()
    test_pomnoz()
    test_podziel()
    print("Wszystkie testy OK")
