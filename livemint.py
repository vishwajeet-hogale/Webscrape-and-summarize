import requests
from bs4 import BeautifulSoup
import pandas as pd
def webscrape():
	url = 'https://www.livemint.com/Search/Link/Keyword/ipo'

	url1 = 'https://www.livemint.com'
	page = requests.get(url)

	soup = BeautifulSoup(page.content, 'html.parser')

	#print(soup)



	links = []

	for a in soup.find_all('h2', {'class': 'headline'}):
		for i in a.find_all('a',href=True):
			#print(i['href'])
			links.append(url1 + i["href"])

	#links.append(a["href"])
	#print(links)

	title = []
	date = []
	s_date = []
	text = []

	for l in links:

		fetch = requests.get(l)
		sp = BeautifulSoup(fetch.content, 'html.parser')
		
		x=sp.find("h1", { "class" : "headline" }).text
		#print(x)

		title.append(x)
		
		y = sp.find("span", { "class" : "articleInfo pubtime" }).text
		#print(y)

		date.append(y)
		
		z = sp.find("div", { "class" : "mainArea" }).text
		#print(z)


		text.append(z)


	df2 = pd.DataFrame(list(zip(title,links,date,text)), 
					columns =['title', 'link','publish_date','text'])


	df2.to_csv('livemint.csv')