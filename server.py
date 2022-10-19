from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

app.secret_key = "keep_main"


@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('index.html')

@app.route('/addtwo')
def dos():
    session['count'] += 1
    return redirect('/')


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


@app.route('/add/number', methods=['POST']) 
def numb():
    numero = int(request.form['cantidad'])
    session['count'] += (numero-1)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)