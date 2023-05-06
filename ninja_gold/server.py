from flask import Flask, session, request, redirect, render_template
import random, datetime
app = Flask(__name__)
app.secret_key = "lskdvjskldf2r2lk4"

@app.route('/', methods=['GET'])
def index():
    if not 'logs' in session:
        session['logs'] = []
        session['trans_color'] = []
    if not 'points' in session:
        session['points'] = 0
    return render_template('index.html')

@app.route('/start_again', methods=['GET'])
def start_again():
    session.clear()
    return redirect('/')

@app.route('/process_money', methods=['POST'])
def process_money():
    now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    trans = get_trans(request)
    if trans >= 0:
        log = f"Earned {trans} golds from the {request.form['which_section']}! ({now})"
        set_info("green", log)
    else:
        log = f"Entered a {request.form['which_section']} and lost {trans} golds... Ouch.. ({now})"
        set_info("red", log)
    return redirect('/')

def get_rand(min, max):
    return random.randint(min, max)

def get_trans(request):
        trans = None
        if request.form['which_section'] == 'Farm':
            trans = get_rand(10,20)
        elif request.form['which_section'] == 'Cave':
            trans = get_rand(5, 10)
        elif request.form['which_section'] == 'House':
            trans = get_rand(2, 5)
        elif request.form['which_section'] == 'Casino':
            trans = get_rand(-50, 50)
        session['points'] += trans
        return trans
    
def set_info(color, log):
    session['trans_color'].append(color)
    session['logs'].append(str(log))

if __name__ == '__main__':
    app.run(debug=True)