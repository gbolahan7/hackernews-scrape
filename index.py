# import requests
# from bs4 import BeautifulSoup

# res = requests.get('https://news.ycombinator.com/news')
# soup = BeautifulSoup(res.text, 'html.parser')

# #Grabbing element with story link
# links = soup.select('.titleline')
# votes = soup.select('.score')

# def create_custom_hn(links, votes):
#     hn = []
#     for idx, item in enumerate(links):
#         title = links[idx].getText()
#         hn.append(title)
#     return hn

# print(create_custom_hn(links, votes).encode("utf-8"))


import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
votes = soup.select('.score')

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.a['href']
        
        if idx < len(votes):
            points_text = votes[idx].getText() 
            points = int(points_text.replace(' points', ''))
            if points > 99:  # only show stories with more than 99 points
                hn.append({'title': title, 'link': href, 'votes': points})
    return sorted(hn, key=lambda x: x['votes'], reverse=True)

custom_hn = create_custom_hn(links, votes)

for item in custom_hn:
    print(item)