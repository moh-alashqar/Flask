from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/')
def level1_play():
    return render_template('index.html', color="#9FC5F8", num = 3)

@app.route('/play/<num>')
def level2_play(num):
    num = int(num)
    return render_template('index.html', num = num, color="#9FC5F8")

@app.route('/play/<num>/<color>')
def level3_play(num = "3", color="#9FC5F8"):
    num = int(num)
    return render_template('index.html', num = num, color = color)

if __name__ == '__main__':
    app.run(debug = True)
