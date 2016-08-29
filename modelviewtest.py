#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from PyQt4 import QtGui
import sys
import stockGUI
import os



class ExampleApp(QtGui.QMainWindow, stockGUI.Ui_MainWindow):

	def __init__(self, parent=None):
		super(ExampleApp, self).__init__(parent)
		self.setupUi(self)
		self.queryButton.clicked.connect(self.browse_folder)


	def browse_folder(self):
		self.tableWidget.clear() #tableWidget is listWidget in original example
		directory = QtGui.QFileDialog.getExistingDirectory(self, 'Pick a folder')

		if directory:
			for file_name in os.listdir(directory):
				self.tableWidget.addItem(file_name) #tableWidget is listWidget in original example



def main():

	app = QtGui.QApplication( sys.argv )
	form = ExampleApp()
	form.show()
	app.exec_()


if __name__ == '__main__':
	main()