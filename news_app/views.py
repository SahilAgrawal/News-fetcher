from django.shortcuts import render
from django.http import JsonResponse
from django.utils.html import format_html

import json

# Create your views here.

def news(requests):
    import bs4
    from bs4 import BeautifulSoup as soup
    from urllib.request import urlopen

    news_url = "https://news.google.com/news/rss"
    try:
        root = urlopen(news_url)
    except:
        return render(requests,'error.html')
    xml_pages = root.read()
    root.close()

    soup_page = soup(xml_pages,"xml")
    # print(type(soup_page))
    context  = soup_page.find_all('item')

    # print(news_list)

    n = []
    for news in context:
        temp = {}
        temp['title'] = news.title.text
        temp['link'] = news.link.text
        temp['date'] = news.pubDate.text
        temp['source'] = news.source.text
        temp['desc'] = format_html(news.description.text)

        n.append(temp)
     

    # print(len(news_list))


    return render(requests, 'index.html', {'data':n})


def about(requests):


    return render(requests, 'about.html')



def developer(requests):


    return render(requests, 'developer.html')


    