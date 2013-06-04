import sqlite3
from bottle import Bottle, route, run, template, post, request, response, static_file, redirect
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