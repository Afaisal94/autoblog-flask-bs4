from flask import Flask, render_template
from webscraping import skysports

app = Flask(__name__)

@app.route('/')
def index():
    data = skysports()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()

# set FLASK_APP=main.py
# set FLASK_ENV=development
# flask run