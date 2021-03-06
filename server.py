from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import ytDL

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/', methods=['POST'])
def albumPost():

    titleList = request.form.getlist('titleValue')
    timeList = request.form.getlist('timeValue')

    if request.form['submit'] == 'Process':
        try:
            downloadLink = request.form['albumURL']

            if not titleList and not timeList:
                ytDL.downloadMp3(downloadLink)
                paths, names = ytDL.songSplit(downloadLink)

                lists = zip(names, paths)

                return render_template('index.html', lists=lists)

            else:
                for time in timeList:
                    for r in ytDL.timeRegex():
                        m = r.match(time)
                        if m:
                            break

                    else:
                        return render_template('index.html')

                ytDL.downloadMp3(downloadLink)
                paths = ytDL.userSongSplit(downloadLink, titleList, timeList)

                names = titleList
                lists = zip(names, paths)

                return render_template('index.html', lists=lists)

        except ValueError:
            return render_template('index.html')

        except IOError:
            return render_template('index.html')

    else:
        try:
            downloadLink = request.form['singleURL']
            temp, filename = ytDL.downloadSingle(downloadLink)

            return redirect(url_for(downloadFunc(filename, temp)))

        except ValueError:
            return render_template('index.html')

        except IOError:
            return render_template('index.html')


@app.route('/Audio/<path:temp>/<path:filename>')
def downloadFunc(filename, temp):

    return send_from_directory("/Audio/", temp + '/' + filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
