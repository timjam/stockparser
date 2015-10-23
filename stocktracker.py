#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This code is not very generic and multipurpose. So far it can only handle these specific urls which were used when designing this code.

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
	#print title


	# Extract the interesting div which contains the <p> "tunnuslukuja"

	rootDiv = data.xpath(".//p[text()='Tunnuslukuja']")[0].getparent()[1] # selects a <p> with text 'Tunnuslukuja', creates a list of it, chooses the first element from the list (it is known that there's only one element) and gets its parent. The [1] at the end then chooses the second child of the original root
	
	texts = []
	values = []

	for element in rootDiv.iter():

		if element.tag == 'tr': 
			pass
			#print ""				# Do nothing when encountering a new row

		if (element.tag == "td") or (element.tag == "br"):
			try:
				print "TAG: " + element.tag
			except AttributeError:
				pass

			try:
				text = element.text.replace(u'\x80', 'e').replace(u'\u20ac', 'e') #For some reason \x80 covers the euro character as well
				print "TEXT: " + text

				texts.append( text )

			except AttributeError:
				pass

			try:
				tail = element.tail.replace(u'\u20ac', 'e')
				print "TAIL: " + tail

				values.append( tail )

			except AttributeError:
				pass

		


main()