# -*- coding: utf_8 -*-

import sqlite3
from user_model import User_model
from auth_model import Auth_model
from message_model import Message_model
from bottle import Bottle, route, run, template, post, request, response, static_file, redirect

app = Bottle()
db = sqlite3.connect('data_new.db')

user_model = User_model(db);
auth_model = Auth_model(db);
message_model = Message_model(db);

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