from flask import Flask, render_template
import random
import os.path

tanzu_quotes = ['Tanzu Rules', 'Tanzu World', 'Tanzu Rocks', 
'Tanzu is Swahili for branches', 'VMware Tanzu']

txt_col = ['yellow', 'brown', 'blue', 'black', 'red']

if os.path.exists('count.txt'):
    pass
else:
    with open('count.txt', 'w') as f:
        f.seek(0)
        f.write('0')

app = Flask(__name__)

@app.route("/")

def index():
    show_text = random.choice(tanzu_quotes)
    head_color = random.choice(txt_col)
    return render_template("index2.html", wordofday = show_text, titlecolor = head_color) 

@app.route("/visitors")

def visitors():
    with open('count.txt', 'r+') as f:
        counter = int(f.read())
        counter += 1
        f.seek(0)
        f.write(str(counter))
        return render_template("visitors.html", num_visitor = counter)


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=80)


