from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    id = request.form['id']
    count = int(strawberry)+int(raspberry)+int(apple)
    print(f"Charging {firstname} {lastname} for {count} fruits")
    return render_template("checkout.html", strawberry=strawberry, raspberry=raspberry, apple=apple, firstname=firstname, lastname=lastname, id=id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    