import urllib2
import os
from bs4 import BeautifulSoup
from stockparser import stockParser

url = "http://www.kauppalehti.fi/5/i/porssi/porssikurssit/osake/?klid=1059"
#sock = open('testhtml.html', 'r')
#feed = sock.read()
#sock.close()

def main():

	clear = lambda: os.system('cls')
	clear()

	sock = urllib2.urlopen( url )
	feed = sock.read()

	#soup = BeautifulSoup(open("testhtml.html"), 'lxml')
	soup = BeautifulSoup( feed, 'lxml' )

	print soup.table

	#interestingBlock = soup.find_all('table', class_="table_stockexchange")

	#print interestingBlock

main()