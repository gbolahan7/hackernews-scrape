import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# # print(soup.body)  #just to grab the body
# print(soup.body.contents)  #just to grab the body and content
# print(soup.find_all('a'))  #just to find all the links


# using selector

# print(soup.select('.score')) # selecting class
# print(soup.select('#score_1234')) # selecting id


#Grabbing element with story link
links = soup.select('.titleline')
votes = soup.select('.score')
# print(votes[0])
print(votes[0].get('id'))