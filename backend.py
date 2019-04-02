"""This is the backend of the movie directory"""

import sqlite3
class Database:
	def __init__(self):
		self.conn=sqlite3.connect("movies.db")
		self.cur=self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS moviesdb (id INTEGER PRIMARY KEY, movie TEXT, genre TEXT, size NUMBER, paths TEXT)")

	def add(self,movie,genre,size,paths):
		self.cur.execute("INSERT INTO moviesdb VALUES (NULL,?,?,?,?)",(movie,genre,size,paths))
		
	def view(self):
		self.cur.execute("SELECT * FROM moviesdb")
		R=self.cur.fetchall()
		return R

	def search(self,movie="",genre=""):
		self.cur.execute("SELECT * FROM moviesdb WHERE movie=? OR genre=?", (movie,genre))
		R=self.cur.fetchall()
		return R

	def delete(self,id):
		self.cur.execute("DELETE FROM moviesdb WHERE id=?",(id,))
		self.conn.commit()
		
	def update(self,id,movie,genre,size,paths):
		self.cur.execute("UPDATE moviesdb SET movie=?, genre=?, size=?, paths=? WHERE id=?",(movie,genre,size,paths,id))
		self.conn.commit()
	