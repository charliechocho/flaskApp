from flask import Flask
import random

tanzu_quotes = ['Tanzu Rules', 'Tanzu World', 'Tanzu Rocks', 'Tanzu is Swahili for branches']

app = Flask(__name__)

@app.route("/")

def hello_name():
    show_text = random.choice(tanzu_quotes)
    return f"{show_text}" 

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=80)
