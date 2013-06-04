import sqlite3
from bottle import Bottle, route, run, template, post, request, response, static_file, redirect
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