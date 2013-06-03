# -*- coding: utf_8 -*-

import sqlite3
import random
from bottle import Bottle, route, run, template, post, request, response, static_file, redirect

app = Bottle()
db = sqlite3.connect('data_new.db')

class User_model:
        def __init__(self, db):
                self.db = db
                self.__create_tables()

        def __create_tables(self):
                cur = self.db.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, login TEXT, email TEXT, password TEXT)')

        def insert(self, login, email, password):
                cur = self.db.cursor()
                try:
                    cur.execute('INSERT INTO users(login, email, password) VALUES(?, ?, ?)', (login, email, password))
                    self.db.commit()
                except sqlite3.Error, e:
                	print "Error %s:" % e.args[0]
                	return False
                return True

        def get(self, login, password = ''):
                cur = self.db.cursor()
                try:
                	if (password):
                		cur.execute('SELECT id, login, email, password FROM users WHERE login=? AND password=?', (login, password))
                	else:
                		cur.execute('SELECT id, login, email, password FROM users WHERE login=?', (login, ))
                	return cur.fetchone()
                except sqlite3.Error, e:
                	print "Error %s:" % e.args[0]
                	return False
               
        def get_id(self, login):
                cur = self.db.cursor()
                cur.execute('SELECT id FROM users WHERE login=?', login)
                row = cur.fetch()
                return row['id']

        def get_list(self):
                cur = self.db.cursor()
                cur.execute('SELECT id, login FROM users')
                return cur.fetchall()

class Auth_model:
        def __init__(self, db):
                self.db = db
                self.__create_tables()
      
        def __create_tables(self):
                cur = self.db.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS auth (user_id INTEGER PRIMARY KEY, hash TEXT)')
        
        def set_code(self, user_id,user_name):
			hash = "%032x" % random.getrandbits(128) 
			response.set_cookie("auth_code", hash, Path='/')
			response.set_cookie("username", user_name, Path='/')
			cur = self.db.cursor()
			cur.execute('INSERT OR REPLACE INTO auth (user_id, hash) VALUES(?, ?)', (user_id, hash))
			self.db.commit()
        
        def delete_code(self):
			code = request.get_cookie("auth_code")
			cur = self.db.cursor()
			cur.execute('DELETE FROM auth WHERE hash=?', (code, ))

        
        def get_user_id(self):
                
			code = request.get_cookie("auth_code")
			
			if code:                
				cur = self.db.cursor()
				cur.execute('SELECT user_id FROM auth WHERE hash=?', (code, ))
				data = cur.fetchone()

				if data:
					return data[0]
				else:
					return False
			else:
				return False

class Message_model:
        def __init__(self, db):
                self.db = db
                self.__create_tables()

        def __create_tables(self):
                cur = self.db.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, from_id INT, data TEXT, date TEXT)')

        def insert(self, message, from_id):
                cur = self.db.cursor()
                cur.execute('INSERT INTO messages(data, from_id, date) VALUES(?, ?, datetime("now"))', (message, from_id))
                self.db.commit()

        def get(self, from_id, to_id, limit):
                cur = self.db.cursor()
                cur.execute('SELECT id, from_id, to_id FROM messages WHERE login=? AND password=?', (login, password))
                return cur.fetch()

        def get_list(self):
                cur = self.db.cursor()
                cur.execute('SELECT m.id, u.login, m.data, m.date FROM messages m, users u WHERE u.id=m.from_id ORDER BY m.id ASC LIMIT 30')
                return cur.fetchall()       

user_model = User_model(db);
auth_model = Auth_model(db);
message_model =Message_model(db);

@app.get('')
@app.get('/')
@app.get('/chat')
def chat():
	user_id = auth_model.get_user_id()
	if user_id:
		return template(get_template('chat',''))
	else:
		redirect('/auth/login')
	
	return template(get_template('chat',''))

@app.post('/chat')
def chat_post():
	user_id = auth_model.get_user_id()
	message_model.insert(request.forms.get('message').decode('utf-8'), user_id)
	return {'result' : 'ok'}

@app.get('/chat/list')
@app.post('/chat/list')
def chat_list():
	messages = message_model.get_list()
	return {'result' : 'ok', 'messages' : messages}


@app.route('/auth/logout')
def logout():
	auth_model.delete_code()
	return template(get_template('logout','auth/'))

@app.post('/auth/login')
def login():
	user = user_model.get(request.forms.get('login'),request.forms.get('password')) 
	if user:
		auth_model.set_code(user[0],request.forms.get('login'))
		return {'result' : 'ok', 'message' : 'Congratulations! You have successfully log in.<br>To chat on go to <a href="/chat">Chat Page</a>'}
	else:
		return {'result' : 'error', 'message' : 'Invalid login or password'}

@app.get('/auth/register')
def register():
	user_id = auth_model.get_user_id()
	if user_id:
		redirect('/chat')
	else:
		return template(get_template('register','auth/'))

@app.get('/auth/login')
def login():
	
	user_id = auth_model.get_user_id()
	if user_id:
		redirect('/chat')
	else:
		return template(get_template('login','auth/'))


@app.post('/auth/register')
def register_post():
	login = request.forms.get('login')
	email = request.forms.get('email')
	password = request.forms.get('password')
	exists = user_model.get(login)
	if exists:
		return {'result' : 'error', 'message' : 'User "' + login + '" already exists'}
	result = user_model.insert(login, email, password)
	if result:
		return {'result' : 'ok', 'message' : 'Congratulations! You have successfully registered.<br>To log on go to <a href="/auth/login">Login Page</a>'}
	return {'result' : 'error', 'message' : 'Server could not insert data into database. Try again later'}
		

def get_template(name,subdir):
	f = open('templates/'+ subdir + name + '.tpl', 'r')
	data = f.read()
	f.close()
	return data
	
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')
	
run(app, host='localhost', port=10101, debug=True)