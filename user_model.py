import sqlite3
from bottle import Bottle, route, run, template, post, request, response, static_file, redirect
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