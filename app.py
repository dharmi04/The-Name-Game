import pandas as pd
import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the DataFrame outside of the route function
df = pd.read_csv("adjective_list.txt", sep=" ")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        
        # Ensure that there are enough rows in the DataFrame to sample from
        if len(df) >= 5:
            adjectives = df.sample(5)['adjective'].tolist()
        else:
            adjectives = ["a", "b", "c", "d", "e"]  # Provide default values if there aren't enough adjectives

        return render_template('result.html', name=name, adjectives=adjectives)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
