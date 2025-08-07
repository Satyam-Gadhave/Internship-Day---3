import requests
from bs4 import BeautifulSoup

url = 'http://zeenews.india.com/latest-news'
r = requests.get(url)

if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')

    titles = []
    title_tag = soup.find('title')
    if title_tag:
        titles.append(title_tag.get_text(strip=True))

    h2_tags = soup.find_all('h2')
    for tag in h2_tags:
        text = tag.get_text(strip=True)
        if text:
            titles.append(text)

    with open('headlines.txt','w', encoding='utf-8') as file:
        for title in titles:
            file.write(title+ "\n")

    print('headlines saved to headlines.txt')

    print('\n fetch headlines:')
    with open('headlines.txt','r', encoding='utf-8') as file:
        headlines = [line.strip() for line in file.readlines()]

    for idx, headline in enumerate(headlines, start=1):
        print(f'{idx}. {headline}')

else:
    print(f"failed to fetch the webpage. status code: {r.status_code}")
