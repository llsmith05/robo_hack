from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Robot - Rapid Prototyping 2014!'

@app.route('/main')
def hello(name=None):
	return render_template('main.html')

@app.route('/view', methods=['GET'])
def View():
	trick = request.args.get('trick', '')
	try:
		distance = int(request.args.get('x', ''))
	except:
		distance = 1

	if trick == "square":
		return render_template('square.html', x=distance)
	elif trick == "straight":
		return render_template('straight.html', x=distance)
	elif trick == "hexagon":
		return render_template('hexagon.html')
	elif trick == "trick":
		return render_template('first_trick.html')
	elif trick == "trick2":
		return render_template('second_trick.html')
	else:
		return render_template('main.html')

@app.route('/fancytrick', methods=['GET'])
def Trick():
	direction = request.args.get('dir', '')
	spintime = request.args.get('time', '')
	return render_template('fancytrick.html', direction=direction, spintime=spintime)

if __name__ == '__main__':
	app.debug = True
	app.run()