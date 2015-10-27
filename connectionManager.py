#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This code is not very generic and multipurpose. So far it can only handle these specific urls which were used when designing this code.

import sqlite3 as sql

class connectionManager():

	dbname = 'stockdata.db'

	def init(self):
		global conn
		global c

		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()

	