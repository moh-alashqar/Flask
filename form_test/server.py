from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     name_from_form = request.form['name']
#     email_from_form = request.form['email']
#     print(f"adding {name_from_form} to the database!")
#     return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)

# we replcaed the above code with the following to solve the resubmission issue
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")

@app.route('/show')
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html", name_on_template=session['username'], email_on_template=session['useremail'])

if __name__ == "__main__":
    app.run(debug = True)