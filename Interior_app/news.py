import requests
from bs4 import BeautifulSoup

class Web_Scraped_news():

	def run():
		page = requests.get("https://timesofindia.indiatimes.com/topic/Property")
		soup = BeautifulSoup(page.content, 'html.parser')
		news = soup.find(id="c_0101")	# The class which contains the given weather info
		coverage = news.find_all(class_="tab_content") #the div which contains the same
		report = coverage[0] #to print info about tonight


		x = report.find(class_ = "content").get_text()

		title = news.select(".tab_content .content")
		heading = [pt.get_text() for pt in title]
		return heading
	# print(heading)