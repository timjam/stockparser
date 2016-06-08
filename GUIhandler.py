#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys
import sqlite3 as sql
from PyQt4 import QtSql
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "C:/Code/GUIs/stockGUI.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class GUIhandler( QtGui.QMainWindow, Ui_MainWindow):

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.queryButton.clicked.connect(self.showEntries)


	def initializeModel(model):
		model.setTable('stockvalues')
		model.setHeaderData(0, QtCore.Qt.Horizontal, "FetchTime")
		model.setHeaderData(1, QtCore.Qt.Horizontal, "StockID")
		model.setHeaderData(2, QtCore.Qt.Horizontal, "Name")
		model.setHeaderData(3, QtCore.Qt.Horizontal, "Price")
		model.setHeaderData(4, QtCore.Qt.Horizontal, "EPS")
		model.setHeaderData(5, QtCore.Qt.Horizontal, "PB")
		model.setHeaderData(6, QtCore.Qt.Horizontal, "PE")
		model.setHeaderData(7, QtCore.Qt.Horizontal, "DpS")
		model.setHeaderData(8, QtCore.Qt.Horizontal, "Marketvalue")


	def showEntries(self):
		conn = sql.connect("stockdata.db")
		cur = conn.cursor()
		for row in self.cur.execute("SELECT * FROM stockvalues"):
			print row
		conn.close()




if __name__== "__main__":

	db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
	db.setDatabaseName("stockdata.db")

	model = QtSql.QSqlTableModel()
	initializeModel(model)

	app = QtGui.QApplication(sys.argv)
	window = GUIhandler()
	window.show()
	sys.exit(app.exec_())