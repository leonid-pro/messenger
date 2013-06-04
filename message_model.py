# -*- coding: utf_8 -*-

import sqlite3
from bottle import Bottle, route, run, template, post, request, response, static_file, redirect
class Message_model:
	def __init__(self, db):
		self.db = db
		self.__create_tables()

	def __create_tables(self):
		cur = self.db.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, from_id INT, data TEXT, date TIMESTAMP)')
		cur.execute('CREATE TABLE IF NOT EXISTS online (user_id INTEGER PRIMARY KEY, date TIMESTAMP)')
	
	def insert(self, message, from_id):
		cur = self.db.cursor()
		cur.execute('INSERT INTO messages(data, from_id, date) VALUES(?, ?, datetime("now"))', (message, from_id))
		self.db.commit()
	
	def get_list(self, user_id):
		self.db.execute('INSERT OR REPLACE INTO online (user_id, date) VALUES(?, datetime("now"))', (user_id, ))
		self.db.commit()
		cur = self.db.cursor()
		cur.execute('SELECT m.id, u.login, m.data, m.date FROM messages m, users u WHERE u.id=m.from_id ORDER BY m.id ASC LIMIT 30')
		return cur.fetchall()  
	
	def get_online(self):
		cur = self.db.cursor()
		cur.execute('SELECT u.login FROM online o, users u WHERE u.id=o.user_id AND strftime("%s", date) - 0 > strftime("%s", "now") - 5')
		return cur.fetchall()  
		pass