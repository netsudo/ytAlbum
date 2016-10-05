from flask import Flask, render_template, request
import ytDL

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def albumPost():

    downloadLink = request.form['albumURL']
    description = ytDL.numberReplace(downloadLink)

    return render_template('index.html', description=description)

if __name__ == '__main__':
    app.run(debug=True)
