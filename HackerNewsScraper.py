import requests
from bs4 import BeautifulSoup
from pprint import pprint

# getting response from the website 
res = requests.get('https://news.ycombinator.com/')
# changes the string from res.text to soup object using html parser
soup = BeautifulSoup(res.text, 'html.parser')
# returns all class having attribute storylink in a list
links = soup.select('.storylink')
# returns all element having attribute subtext that contain points in a list
subtext =  soup.select('.subtext')


def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key= lambda k:k['votes'], reverse=True)


def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hn)

pprint(create_custom_hn(links, subtext))