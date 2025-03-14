from flask import Flask, render_template, request

app = Flask(__name__)

def get_greeting(lang):
    translations = {
        "pt": "Olá, Mundo!",
        "en": "Hello, World!",
        "es": "¡Hola, Mundo!",
        "fr": "Bonjour, le Monde!",
        "de": "Hallo, Welt!",
        "it": "Ciao, Mondo!",
        "jp": "こんにちは、世界！",
        "ru": "Привет, мир!",
        "zh": "你好，世界！"
    }
    return translations.get(lang, "Idioma não suportado")

@app.route("/", methods=["GET", "POST"])
def index():
    greeting = ""
    if request.method == "POST":
        language = request.form.get("language")
        greeting = get_greeting(language)
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run(debug=True)
