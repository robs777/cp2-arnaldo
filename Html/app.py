from flask import Flask, render_template, request,url_for
import requests


app = Flask(__name__)

@app.route('/receitas')
def receitas():
    response = requests.get('https://gold-anemone-wig.cyclic.app/receitas/todas')
    data = response.json()
    return render_template('receitas.html', receitas=data)

if __name__ == '__main__':
    app.run()

