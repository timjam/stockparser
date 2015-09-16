import urllib2
from stockparser import stockParser

testurl = "http://www.kauppalehti.fi/5/i/porssi/porssikurssit/osake/?klid=1059"
url = testur

def main():
	response = urllib.urlopen( url )
	feed = response.read()
	parser = stockParser()

main()