def na_wielkie(tekst):
    return tekst.upper()

def na_male(tekst):
    return tekst.lower()

def policz_slowa(tekst):
    if not tekst.strip():
        return 0
    return len(tekst.split())

def odwroc(tekst):
    return tekst[::-1]
