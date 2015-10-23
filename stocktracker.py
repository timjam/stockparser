#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import os
from stockparser import stockParser
from lxml import etree

url = "http://www.kauppalehti.fi/5/i/porssi/porssikurssit/osake/?klid=1059" #Wärtsilä
url2 = "http://www.kauppalehti.fi/5/i/porssi/porssikurssit/osake/?klid=1091" #Sanoma

def main():

	os.system('cls')

	sock = urllib2.urlopen( url )
	feed = sock.read()


	#etree testing here

	data = etree.HTML(feed) #Converts the html feed to etree, that can be traversed by xpath expressions

	# Extract the title
	titletag = data.xpath('//head/title/text()') #Selects the text from the first title inside the <head> tags
	title = titletag[0].split("|")[0] #Takes the one and only element returned by the above line, splits it by the character "|", creates the new list from the splitted elements and chooses the first element, which is known to be the name of the stock
	print title


	# Extract the interesting div which contains the <p> "tunnuslukuja"

	rootDiv = data.xpath(".//p[text()='Tunnuslukuja']")[0].getparent() # selects a <p> with text 'Tunnuslukuja', creates a list of it, chooses the first element from the list (it is known that there's only one element) and gets its parent

	#print rootDiv.tag, rootDiv.attrib

	el = rootDiv[1][0][0][0]

	try:
		print "TAG: " + el.tag
	except TypeError:
		print "TAG: None"

	try:
		print "\nTEXT: " + el.text
	except TypeError:
		print "TEXT: None"

	try:
		print "\nTAIL: " + el.tail.replace(u'\u20ac', 'e')
	except TypeError:
		print "TAIL: None"



	for element in rootDiv.iter():

		if element.tag == 'ul': 
			break 					# It is known that in this html chunk all the interesting data is parsed when we encounter first ul tag

		if element.tag == 'tr': 
			print ""				# Do nothing when encountering a new row

		if element.tag == 'td' or 'br':
			try:
				print element.tag
			except AttributeError:
				pass

			try:
				print element.text.encode('utf8')
			except AttributeError:
				pass

			try:
				print element.tail.encode('utf8')
			except AttributeError:
				pass


	#print
	#print
	#print etree.tostring(rootDiv, pretty_print=True)

		


main()