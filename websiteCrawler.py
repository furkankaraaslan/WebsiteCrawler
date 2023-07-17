import requests
from bs4 import BeautifulSoup


target_url = "https://news.ycombinator.com/"
found_links = []


def make_request(t_url):
    try:
        response = requests.get(t_url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    except requests.exceptions.ConnectionError:
        pass


links = make_request(target_url)
for link in links.find_all('a'):
    found_link = link.get('href')
    if found_link is not None:
        if "https://" in found_link or "http://" in found_link:
            found_links.append(found_link)


news_list = found_links[1:-3]

with open("News List.txt", "w") as news_text_list:
    for i in range(len(news_list)):
        news_text_list.write(news_list[i] + "\n")
