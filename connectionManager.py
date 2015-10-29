#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This code is not very generic and multipurpose. So far it can only handle these specific urls which were used when designing this code.

import sqlite3 as sql

class connectionManager():

	dbname = 'stockdata.db'
	global conn
	global c
	

	def init(self):

		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS stockvalues (stocknumber, stockname, curprice, eps, pb, pe, dps, marketvalue)")

	

	def dbinsert(self, values):

		cursor.execute("INSERT INTO stockvalues VALUES (?,?,?,?,?,?,?,?)", values)
		conn.commit



	def dbshow(self):

		for row in cursor.execute("SELECT * FROM stockvalues"):
			print row



	def dbclose():

		conn.close()