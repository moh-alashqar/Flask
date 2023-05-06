from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe'

@app.route('/', methods=['GET'])
def main():
    session.clear()
    session['random_number'] = random.randint(0, 100)
    return render_template('main.html')

@app.route('/process', methods=['POST'])
def process():
    guessed_number = request.form['guessed_number']
    random_number = session['random_number']
    if 'attempts' in session:
        session['attempts'] += 1
    else: 
        session['attempts'] = 1
    if session['attempts'] == 5:
        session['status'] = "You lose!"
        session['color'] = "red"
        session['done'] = True
        return redirect ('/result')
    else:
        try:
            guessed_number = int(guessed_number)
            if guessed_number <= 100 and guessed_number >= 1:
                if guessed_number == random_number:
                    session['status'] = f"{guessed_number} was the number!"
                    session['color'] = "green"
                    session['done'] = True
                    return redirect ('/result')
                elif guessed_number - random_number > 50:
                    session['status'] = "Too high!"
                    session['color'] = "red"
                    session['done'] = False
                    return redirect ('/result')
                elif guessed_number - random_number > 25:
                    session['status'] = "High!"
                    session['color'] = "red"
                    session['done'] = False
                    return redirect ('/result')
                elif guessed_number - random_number > 10:
                    session['status'] = "Close!"
                    session['color'] = "orange"
                    session['done'] = False
                    return redirect ('/result')
                elif guessed_number > random_number:
                    session['status'] = "Too close!"
                    session['color'] = "yellow"
                    session['done'] = False
                    return redirect ('/result')
                elif random_number - guessed_number > 50:
                    session['status'] = "Too low!"
                    session['color'] = "red"
                    session['done'] = False
                    return redirect ('/result')
                elif random_number - guessed_number > 25:
                    session['status'] = "Low!"
                    session['color'] = "red"
                    session['done'] = False
                    return redirect ('/result')
                elif random_number - guessed_number > 10:
                    session['status'] = "Close!"
                    session['color'] = "orange"
                    session['done'] = False
                    return redirect ('/result')
                elif random_number > guessed_number:
                    session['status'] = "Too close!"
                    session['color'] = "yellow"
                    session['done'] = False
                    return redirect ('/result')
            else:
                session['status'] = "Please Enter an intger between 1 and 100 !"
                session['color'] = "red"
                session['done'] = False
                return redirect ('/result')
        except Exception:
                session['status'] = "Integers only allowed!"
                session['color'] = "red"
                session['done'] = False
                return redirect ('/result')

@app.route('/result')
def result():
    return render_template('result.html', result = session['status'], color = session['color'], done = session['done'], attempts = session['attempts'])

@app.route('/end')
def end():
    session.clear()
    return redirect ('/')

if __name__ == '__main__':
    app.run(debug=True)

# REST API
# Angular
# 