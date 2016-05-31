#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This code is not very generic and multipurpose. So far it can only handle these specific urls which were used when designing this code.

import sqlite3 as sql

class connectionManager(object):
	

	def __init__(self, db):

		self.conn = sql.connect(db)
		self.conn.execute("CREATE TABLE IF NOT EXISTS stockvalues (fetchtime, stocknumber, stockname, curprice, eps, pb, pe, dps, marketvalue)")
		self.conn.commit()
		self.cur = self.conn.cursor()

	

	def dbinsert(self, values):

		self.cur.execute("INSERT INTO stockvalues VALUES (?,?,?,?,?,?,?,?,?)", values)
		self.conn.commit()

		#c = sql.connect(self.dbname).cursor()
		#c.execute("INSERT INTO stockvalues VALUES (?,?,?,?,?,?,?,?)", values)
		#c.commit



	def dbshow(self):

		for row in self.cur.execute("SELECT * FROM stockvalues"):
			print row



	def dbclose(self):

		self.conn.close()