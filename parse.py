import requests
from bs4 import BeautifulSoup
import csv


r = requests.get("https://en.wikipedia.org/wiki/2017%E2%80%9318_Olympique_Lyonnais_season")

htmlcontent = str(r.content).split('<h2>')
for s in htmlcontent:
	if '<span class="mw-headline" id="Competitions">' in s:
		comprecord = s




creccontent = comprecord.split('<h3>')

with open('att.csv', 'a', newline='') as csvfile:
	fieldnames = ['Competition', 'Matchday', 'Date', 'Home', 'Away', 'Position', 'Attendance']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	#writer.writeheader()
	date = None
	td = None
	away = None
	for s in creccontent:
		if 'Results by' in s:
			stable = BeautifulSoup(s, 'html.parser')
			td = stable.find("td", string="Position")
			
		soup = BeautifulSoup(s, 'html.parser')
		for t in soup.find_all("span", class_="mw-headline"):
			if 'h4' not in t.parent.name:
				#print(t.string)
				comp = t.string
				mday = 1
			
		for t in soup.find_all("br"):
			if "Attendance" in t.nextSibling:
				#print("Mday", mday)
				flag = 0
				for tag in t.parent.parent.parent.find_all("td"):
					if tag.span and ("2017" in tag.span.contents[0] or "2018" in tag.span.contents[0]):	
						#print(tag.span.string)
						date = tag.span.contents[0]
					if 'class' in tag.attrs:
						for t2 in tag.find_all('span'):
							if t2.contents[0].string:
								#print(t2.string)
								if flag==0:
									home = t2.contents[0].string
									flag=1
								else:
									away = t2.contents[0].string
					
								
				#print(t.nextSibling.split(' ')[2])
				att = t.nextSibling.split(' ')[2]
				pos = None
				if td:
					while td.nextSibling:
						if td.nextSibling.name:
							#print(td.nextSibling.string[:1])	
							pos = td.nextSibling.string[:1]	
							td = td.nextSibling
							break
						else:
							td = td.nextSibling
						
				writer.writerow({'Competition' : comp, 'Matchday' : mday, 'Date' : date, 'Home' : home, 'Away' : away, 'Position' : pos, 'Attendance' : att})
				mday +=1
	
