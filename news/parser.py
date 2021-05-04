from bs4 import BeautifulSoup as BS
import requests as req

#from osiris.settings import PARSLIMIT
PARSLIMIT = 20
from loguru import logger

def get_tabpdf(url):
    logger.warning(url)
    resp = req.get(url)
    soup = BS(resp.text, 'html.parser')
    domain = (url.split('https://')[1].strip('/'))

    if 'fingertabs.com' in domain:
        pdf_div = soup.find('iframe', class_='pdfjs-viewer')
        if pdf_div:
            return pdf_div['src']
    
def news_text(url):
    logger.warning(url)
    resp = req.get(url)
    soup = BS(resp.text, 'html.parser')
    domain = (url.split('https://')[1].strip('/'))

    new_text = ''

    if 'www.theverge.com' in domain:
        text_div = soup.find('div', class_="c-entry-content")
        if text_div:
            p_div = text_div.find_all('p')
            for p in p_div:
                new_text += ((p.text) + ('\n\n'))
    
    if 'ria.ru' in domain:
        text_div = soup.find_all('div', class_="article__text")
        for div in text_div:
            new_text += ((div.text) + ('\n\n'))
            
    return new_text

def parse_news(url):
    resp = req.get(url)
    soup = BS(resp.text, 'html.parser')
    domain = (url.split('https://')[1].strip('/'))

    logger.debug(domain)

    total = []

    if domain == 'www.theverge.com':
        divs = soup.find_all('div', class_="c-entry-box--compact__body")
        
        limit = 0
        if len(divs) < PARSLIMIT:
            limit = len(divs)
        else:
            limit = PARSLIMIT
        logger.success('Parselimit: ' + str(limit))
        
        for div in divs[:limit]:
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

    elif domain == 'ria.ru':
        divs = soup.find_all('a', class_="cell-list__item-link color-font-hover-only")
        
        limit = 0
        if len(divs) < PARSLIMIT:
            limit = len(divs)
        else:
            limit = PARSLIMIT
            
        logger.success('Parselimit: ' + str(limit))

        for div in divs[:limit]:
            if div:
                post_title = div['title']
                post_link = div['href']
                post_text = news_text(post_link)
                
                total.append({
                    "link": post_link,
                    "title": post_title,
                    "text": post_text
                })

    elif domain == 'fingertabs.com':
        divs = soup.find_all('div', class_="post-content")

        limit = 0
        if len(divs) < PARSLIMIT:
            limit = len(divs)
        else:
            limit = PARSLIMIT
        
        logger.success('Parselimit: ' + str(limit))

        for div in divs[:limit]:
            if div:
                tab_link = div.h2.a['href']
                tab_name = div.h2.text.replace('fingerstyle tabs ', '')
                tab_pdf = get_tabpdf(tab_link)

                total.append({
                    "name": tab_name,
                    "link": tab_link,
                    "pdf": tab_pdf
                })
    
    return total

