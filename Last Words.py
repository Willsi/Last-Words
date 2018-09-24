from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import requests
import time
import os
import codecs
file1=codecs.open("Last.txt", "r+" , "utf-8")

r ="https://en.wikiquote.org/wiki/Last_words"
headers = {'User-Agent': 'Mozilla/5.0'}
start_url = requests.get(r,headers=headers)
soup = BeautifulSoup(start_url.text, 'html.parser')

		
text = soup.find('div', class_='mw-content-ltr')

x=0
t=0
while (t==0):
	
	quotes = text.findAll('li')[x].text
	
		
	x=x+1
	print(quotes)

	print("\n")
	print("\n")
	try:
		file1.write(quotes + os.linesep)
		file1.write(os.linesep)
		
	
		continue
	except:
		continue
	
	


