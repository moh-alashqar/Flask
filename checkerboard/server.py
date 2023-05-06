from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def standard_checkerboard():
    return render_template("index.html", x = 8, y = 8, color0 = "black", color1 = "red")

@app.route('/4')
def four_checkerboard():
    return render_template("index.html", x = 8, y = 4, color0 = "black", color1 = "red")

@app.route('/<x>/<y>')
def custom_checkerboard(x,y):
    try:
        x = int(x)
        y = int(y)
        return render_template('index.html', x = x, y = y, color0 = "black", color1 = "red")
    except ValueError:
        return "X and Y must be integers!"

@app.route('/<x>/<y>/<color0>/<color1>')
def color_custom_checkerboard(x, y, color0, color1):
    try:
        x = int(x)
        y = int(y)
        color0 = color0
        color1 = color1
        return render_template('index.html', x = x, y = y, color0 = color0, color1 = color1)
    except ValueError:
        return "X and Y must be integers!"

if __name__ == '__main__':
    app.run(debug=True)