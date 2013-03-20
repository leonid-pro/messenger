from bottle import Bottle, route, run, template, post, request
#import sqlite3

app = Bottle()

@app.route('/chat')
def chat():
	return template(get_template('chat'))

@app.post('/chat/put-message')
def put_message():
	message = request.forms.get('message')
	return message

def get_template(name):
	f = open('templates/' + name + '.tpl', 'r')
	data = f.read()
	f.close()
	return data	
	

run(app, host='localhost', port=10100, debug=True)