from flask import Flask, request, redirect, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pokemon_python.html')

app.run(debug=True)
