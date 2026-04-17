def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b == 0:
        return "Blad: dzielenie przez zero"
    return a / b

if __name__ == "__main__":
    print(dodaj(2, 3))
    print(odejmij(10, 4))
    print(pomnoz(3, 5))
    print(podziel(10, 2))
