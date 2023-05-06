from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route('/', methods=['GET'])
def signup_show():
    return render_template('signup.html')

@app.route('/process', methods=['POST'])
def signup_process():
    print("Got Post Info!")
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    lang = request.form['lang']
    comment = request.form['comment']
    try:
        m_status = request.form['m_status']
    except KeyError:
        m_status = "None"
    try:
        ninja = request.form['ninja']
        ninja = "Yes"
    except KeyError:
        ninja = "No"
    return render_template('show_info.html', name = name, location = location, lang = lang, comment = comment, m_status = m_status,ninja =ninja)


if __name__ == '__main__':
    app.run(debug=True)