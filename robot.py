from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Robot - Rapid Prototyping 2014!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/robot/go/')
@app.route('/robot/go/<x>')
def StraightLine(x=1):
	x = int(x)
	return render_template('straight.html', x=x)

@app.route('/robot/square/')
@app.route('/robot/square/<x>')
def Square(x=1):
	x = int(x)
	return render_template('square.html', x=x)

if __name__ == '__main__':
	app.debug = True
	app.run()