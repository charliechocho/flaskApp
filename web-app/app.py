from flask import Flask, render_template
import random

tanzu_quotes = ['Tanzu Rules', 'Tanzu World', 'Tanzu Rocks', 
'Tanzu is Swahili for branches', 'VMware Tanzu']

app = Flask(__name__)

@app.route("/")

def index():
    show_text = random.choice(tanzu_quotes)
    return render_template("index2.html", wordofday = show_text) 

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=80)
