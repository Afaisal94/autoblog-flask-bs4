from bs4 import BeautifulSoup
from lxml import etree
import requests

def skysports():
    url = 'https://www.skysports.com/football'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    dom = etree.HTML(str(soup))
    titles = dom.xpath("//a[@class='news-list__figure']")
    snippets = dom.xpath("//div[@class='news-list__body']/p")
    imgs = dom.xpath("//a[@class='news-list__figure']/div/img")

    count = len(titles)

    data = []

    for x in range(count):
        title = titles[x].attrib.get('title')
        link = titles[x].attrib.get('href')
        img = imgs[x].attrib.get('data-src')
        snippet = snippets[x].text
        article = get_article(link)
        content = {
            "id": x,
            "title": title,
            "link": link,
            "img": img,
            "snippet": snippet,
            "article": article
        }
        data.append(content)

    return data

def get_article(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    dom = etree.HTML(str(soup))
    articles = dom.xpath("//div[@class='sdc-article-body sdc-article-body--lead']/p")

    count = len(articles)

    data = ''

    for x in range(count):
        article = articles[x].text
        if article is not None:
            data = data + str(article) + '<br><br> '

    return data