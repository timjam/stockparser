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

	#soup = BeautifulSoup(open("testhtml.html"), 'lxml')
	soup = BeautifulSoup( feed, 'lxml' )

	interestingDiv = soup.find_all("p", text="Tunnuslukuja")

	print interestingDiv

	#for elems in interestingDiv:
	#	for row in elems.find_all("p", text="Tunnuslukuja"):
	#		print row



	#interestingBlock = soup.find_all('table', class_="table_stockexchange")

	#print interestingBlock

main()