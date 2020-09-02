from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is home page for no path, <h1> Welcome Home</h1>'

@app.route('/about')
def about():
    return '<h1>This is my about page</h1>'

@app.route('/error')
def error():
    return '<h1>Either you encountered an error or you are not authorized.</h1>'

@app.route('/hello')
def hello():
    return '<h1>Hello World!!!</h1>'

@app.route("/admin")
def admin():
    return redirect("/error")     #return redirect(url_for('error')) bu da oluyor.
    
#@app.route('/<name>')
#def greet(name):
#    return f'Hello, { name }'

#@app.route('/<name>')
#def greet(name):
#    greet_format=f"""
#!DOCTYPE html>
#<html>
#<head>
#    <title>Greeting Page</title>
#</head>
#<body>
#    <h1>Hello, { name }!</h1>
#    <h1>Welcome to my Greeting Page</h1>
#</body>
#</html>
#    """
#    return greet_format

@app.route('/greet-admin')
def greet_admin():
    return redirect(url_for('greet', name = 'Master Admin!!!!'))

@app.route('/<name>')
def greet(name):
    return render_template('greet.html', isim = name)

@app.route('/list100')
def evens():
    return render_template('list100.html')

@app.route('/evens')
def list100():
    return render_template('evens.html')


      


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)