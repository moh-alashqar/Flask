from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'sfdgkADFGHdgDTU445^^iadmfgADFGGJVA$534534590@$#knmodfg'

@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:   
        session['visits'] = 1
    return render_template('index.html', visits=session['visits'])

@app.route('/add_two')
def add_two():
    session['visits'] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.pop('visits')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)