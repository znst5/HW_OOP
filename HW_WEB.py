import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

def get_result(queries):
  habr_blog = pd.DataFrame()
  for query in queries:
    URL = 'https://habr.com/ru/search/?q='
    params = {
        'q': query,
        }
    res = requests.get(URL, params = params)
    time.sleep(0.3)
    soup = BeautifulSoup(res.text, features="html.parser")
    articles = soup.find_all('article', class_ = 'tm-articles-list__item')
    for article in articles:
      date = article.find('a', class_ = ['tm-article-datetime-published tm-article-datetime-published_link']).text
      title = article.find('h2', class_ = ['h2', 'tm-title tm-title_h2']).text
      link = 'https://habr.com' + article.find('a', 'tm-title__link').get('href')
      check = requests.head(link)
      if check.status_code != 200:
        link = 'NaN'
      row = {'date': date, 'title': title, 'link': link}
      habr_blog = pd.concat([habr_blog, pd.DataFrame([row])])
  return habr_blog[habr_blog.link != 'NaN'].reset_index(drop=True)

get_result(['дизайн', 'фото', 'web', 'python'])