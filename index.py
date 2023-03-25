from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


app.run('127.0.0.1', port=8000)
