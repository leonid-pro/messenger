import sqlite3
from bottle import Bottle, route, run, template, post, request, static_file

app = Bottle()

class User_model:
        def __init__(self):
                self.db = sqlite3.connect('data.db')
                self.__create_tables()

        def __create_tables(self):
                cur = self.db.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, login TEXT, password TEXT)')

        def insert(self, login, password):
                cur = self.db.cursor()
                try:
                    cur.execute('INSERT INTO users(login, password) VALUES(?, ?)', (login, password))
                    self.db.commit()
                except:
                    return False
                return True

        def get(self, login, password):
                cur = self.db.cursor()
                cur.execute('SELECT id, login, password FROM users WHERE login=? AND password=?', (login, password))
                return cur.fetch()

        def get_id(self, login):
                cur = self.db.cursor()
                cur.execute('SELECT id FROM users WHERE login=?', login)
                row = cur.fetch()
                return row['id']

        def get_list(self):
                cur = self.db.cursor()
                cur.execute('SELECT id, login FROM users')
                return cur.fetchall()

class Message_model:
        def __init__(self):
                self.db = sqlite3.connect('data.db')
                self.__create_tables()

        def __create_tables(self):
                cur = self.db.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, from_id INT, to_id INT, data TEXT)')

        def insert(self, message, from_id, to_id):
                cur = self.db.cursor()
                cur.execute('INSERT INTO messages(data, from_id, to_id) VALUES(?, ?, ?)', (message, from_id, to_id))
                self.db.commit()

        def get(self, from_id, to_id, limit):
                cur = self.db.cursor()
                cur.execute('SELECT id, from_id, to_id FROM messages WHERE login=? AND password=?', (login, password))
                return cur.fetch()

        def get_list(self):
                cur = self.db.cursor()
                cur.execute('SELECT id, login FROM users')
                return cur.fetchall()       


user_model = User_model();

@app.route('/')
@app.route('/chat')
def chat():
	return template(get_template('chat',''))
	
@app.route('/auth')
def chat():
	return template(get_template('login','login/'))

@app.post('/auth/login')
def login():
	isSuccess = user_model.insert(request.forms.get('login'),request.forms.get('password')) 
	if isSuccess:
		return template(get_template('login-success','login/'))
	else:
		return template(get_template('login-failed','login/'))

@app.post('/login/register')
def register():
	return template(get_template('login','login/'))

@app.post('/chat/put-message')
def put_message():
	message = request.forms.get('message')
	return message

def get_template(name,subdir):
	f = open('templates/'+ subdir + name + '.tpl', 'r')
	data = f.read()
	f.close()
	return data
	
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')
	
run(app, host='localhost', port=10100, debug=True)