from flask import Flask, render_template, request, send_from_directory
import ytDL

app = Flask(__name__, static_folder='Audio', static_url_path='')

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def albumPost():

    downloadLink = request.form['albumURL']
    ytDL.downloadMp3(downloadLink)
    paths, names = ytDL.songSplit(downloadLink)

    lists = zip(names, paths)

    return render_template('index.html', lists=lists)

@app.route('/Audio/<path:temp>/<path:filename>')
def downloadFunc(filename, temp):

    return send_from_directory(app.static_folder, temp + '/' + filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
