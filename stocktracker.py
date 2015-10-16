#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import os
from bs4 import BeautifulSoup
from stockparser import stockParser
from lxml import etree

url = "http://www.kauppalehti.fi/5/i/porssi/porssikurssit/osake/?klid=1059" #Wärtsilä
url2 = "http://www.kauppalehti.fi/5/i/porssi/porssikurssit/osake/?klid=1091" #Sanoma
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

	# Extract the title
	titletag = data.xpath('//head/title/text()') #Selects the text from the first title inside the <head> tags
	title = titletag[0].split("|")[0] #Takes the one and only element returned by the above line, splits it by the character "|", creates the new list from the splitted elements and chooses the first element, which is known to be the name of the stock
	print title


	# Extract the interesting div "tunnuslukuja"

	#rootDiv = data.xpath("//div[contains(@class='white_box')]/p[@text='Tunnuslukuja']")
	rootDiv = data.xpath(".//div[@class='box_white' and ./p[contains(., 'Tunnuslukuja')]]")

	for element in rootDiv:
		print element.tag, element.attrib

	#print rootDiv.tag, rootDiv.attrib

	#rootDiv2 = data.xpath("/p[text()='Tunnuslukuja']/..")
	rootDiv2 = data.xpath(".//p[text()='Tunnuslukuja']")


	for el in rootDiv2:
		print el.tag, el.attrib, el.text, el.getparent().tag, el.getparent().attrib


	# BFSoup things here

	#soup = BeautifulSoup(open("testhtml.html"), 'lxml')
	soup = BeautifulSoup( feed, 'lxml' )

	title = soup.find("title")
	stockname = soup.find("div", {"id": "EAS_11667"})
	interestingDiv = soup.find_all("p", text="Tunnuslukuja")

	#print interestingDiv
	#print stockname
	#print title

	#for elems in interestingDiv:
	#	for row in elems.find_all("p", text="Tunnuslukuja"):
	#		print row



	#interestingBlock = soup.find_all('table', class_="table_stockexchange")

	#print interestingBlock

main()