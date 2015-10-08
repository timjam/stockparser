#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import os
from bs4 import BeautifulSoup
from stockparser import stockParser
from lxml import etree

url = "http://www.kauppalehti.fi/5/i/porssi/porssikurssit/osake/?klid=1059"
#sock = open('testhtml.html', 'r')
#feed = sock.read()
#sock.close()

def main():

	os.system('cls')
	#clear = lambda: os.system('cls')
	#clear()

	sock = urllib2.urlopen( url )
	feed = sock.read()

	#etree testing here
	data = etree.HTML(feed) #Converts the html feed to etree, that can be traversed by xpath expressions
	div = data.xpath('//head/title/text()') #Selects the text from the first title inside the <head> tags
	print div[0].split("|")[0] #Takes the one and only element returned by the above line, splits it by the character "|", creates the new list from the splitted elements and chooses the first element, which is known to be the name of the stock

	#soup = BeautifulSoup(open("testhtml.html"), 'lxml')
	soup = BeautifulSoup( feed, 'lxml' )

	title = soup.find("title")
	stockname = soup.find("div", {"id": "EAS_11667"})
	interestingDiv = soup.find_all("p", text="Tunnuslukuja")

	print interestingDiv
	print stockname
	print title

	#for elems in interestingDiv:
	#	for row in elems.find_all("p", text="Tunnuslukuja"):
	#		print row



	#interestingBlock = soup.find_all('table', class_="table_stockexchange")

	#print interestingBlock

main()