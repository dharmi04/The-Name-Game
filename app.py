import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Load long sentences from the text file into a list with UTF-8 encoding
with open("adjective_list1.txt", "r", encoding="utf-8") as file:
    long_sentences = [line.strip() for line in file]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']

        # Randomly select a long sentence
        long_sentence = random.choice(long_sentences)

        return render_template('result.html', name=name, sentence=long_sentence)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
