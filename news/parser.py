from bs4 import BeautifulSoup as BS
import requests as req

from osiris.settings import PARSLIMIT

from loguru import logger

def news_text(url):
    resp = req.get(url)
    soup = BS(resp.text, 'html.parser')
    text_div = soup.find('div', class_="c-entry-content")
    if text_div:
        p_div = text_div.find_all('p')
        new_text = ''
        for p in p_div:
            new_text += ((p.text) + ('\n\n'))
        return new_text

def parse_news(url):
    resp = req.get(url)
    soup = BS(resp.text, 'html.parser')
    domain = (url.split('https://www.')[1].strip('/'))

    total = []
    if domain == 'theverge.com':
        divs = soup.find_all('div', class_="c-entry-box--compact__body")
        
        for div in divs[:PARSLIMIT]:
            if div:
                header = div.find('h2')
                a_block = header.find('a')

                post_link = ''
                post_title = ''
                post_text = ''
                
                if a_block:
                    post_link = a_block['href']
                    post_title = a_block.text
                    post_text = news_text(post_link)
                
                total.append({
                    "link": post_link,
                    "title": post_title,
                    "text": post_text
                })

    return total

"""

news = parse_news("https://www.theverge.com/")
count = 0
for new in news:
    logger.warning(new['title'])
    count += 1
logger.error(count)

"""