from flask import Flask, request, render_template_string
from tools import na_wielkie, na_male, policz_slowa, odwroc

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <title>Narzedzia tekstowe</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 0 20px; background: #f5f5f5; }
    h1 { color: #333; }
    textarea { width: 100%; height: 100px; padding: 8px; font-size: 14px; box-sizing: border-box; }
    .buttons { margin: 10px 0; display: flex; gap: 8px; flex-wrap: wrap; }
    button { padding: 8px 16px; background: #4a90d9; color: white; border: none; border-radius: 4px; cursor: pointer; }
    button:hover { background: #357abd; }
    .wynik { margin-top: 20px; padding: 12px; background: white; border-left: 4px solid #4a90d9; border-radius: 2px; }
    .wynik h3 { margin: 0 0 8px 0; color: #555; font-size: 13px; text-transform: uppercase; }
    .wynik p { margin: 0; font-size: 16px; word-break: break-word; }
  </style>
</head>
<body>
  <h1>Narzedzia tekstowe</h1>
  <form method="POST">
    <textarea name="tekst" placeholder="Wpisz lub wklej tekst...">{{ tekst or '' }}</textarea>
    <div class="buttons">
      <button name="akcja" value="wielkie">WIELKIE LITERY</button>
      <button name="akcja" value="male">małe litery</button>
      <button name="akcja" value="slowa">Policz słowa</button>
      <button name="akcja" value="odwroc">Odwróć tekst</button>
    </div>
  </form>
  {% if wynik is not none %}
  <div class="wynik">
    <h3>Wynik</h3>
    <p>{{ wynik }}</p>
  </div>
  {% endif %}
</body>
</html>"""

AKCJE = {
    'wielkie': na_wielkie,
    'male': na_male,
    'slowa': lambda t: str(policz_slowa(t)),
    'odwroc': odwroc,
}

@app.route('/', methods=['GET', 'POST'])
def index():
    wynik = None
    tekst = ''
    if request.method == 'POST':
        tekst = request.form.get('tekst', '')
        akcja = request.form.get('akcja', '')
        if akcja in AKCJE:
            wynik = AKCJE[akcja](tekst)
    return render_template_string(HTML, wynik=wynik, tekst=tekst)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
