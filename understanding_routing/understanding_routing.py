from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}!"

@app.route('/repeat/<num>/<txt>')
def repeat(txt, num):
    try:
        return (txt + " ") * int(num)
    except ValueError: 
        return "Ops! The number of repetition must be integer!"

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No Response. Try again"

if __name__ == '__main__':
    app.run(debug=True)