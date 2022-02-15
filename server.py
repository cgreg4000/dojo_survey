from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'Oreo'

@app.route('/')
def survey():
    session.clear()
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'go-back' in request.form:
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', name = session['name'], location = session['location'], language = session['language'], comment = session['comment'])

if __name__=="__main__":
    app.run(debug=True)