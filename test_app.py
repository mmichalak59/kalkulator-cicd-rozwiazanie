from tools import na_wielkie, na_male, policz_slowa, odwroc

def test_na_wielkie():
    assert na_wielkie("hello") == "HELLO"
    assert na_wielkie("Ala ma kota") == "ALA MA KOTA"
    assert na_wielkie("") == ""

def test_na_male():
    assert na_male("HELLO") == "hello"
    assert na_male("Ala MA KOTA") == "ala ma kota"

def test_policz_slowa():
    assert policz_slowa("jeden dwa trzy") == 3
    assert policz_slowa("jedno") == 1
    assert policz_slowa("") == 0
    assert policz_slowa("   ") == 0

def test_odwroc():
    assert odwroc("abc") == "cba"
    assert odwroc("hello") == "olleh"
    assert odwroc("") == ""

if __name__ == "__main__":
    test_na_wielkie()
    test_na_male()
    test_policz_slowa()
    test_odwroc()
    print("Wszystkie testy OK")
