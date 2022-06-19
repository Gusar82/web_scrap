"""Задача 1: Необходимо парсить страницу со свежими статьями (https://habr.com/ru/all/) и выбирать те статьи,
   в которых встречается хотя бы одно из ключевых слов (эти слова определяем в начале скрипта).
   Поиск вести по всей доступной preview-информации (это информация, доступная непосредственно с текущей страницы).
   Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>.

   Задача 2: Улучшить скрипт так, чтобы он анализировал не только preview-информацию статьи,
   но и весь текст статьи целиком."""

from requests import get
import bs4
from header import HEADERS


def get_soup(url, header):
    responce = get(url, headers=header)
    text = responce.text
    return bs4.BeautifulSoup(text, features='html.parser')


def get_articles_previw(soup):
    pass


def search_keywords(article):
    pass


def get_date_articles(soup):
    pass


def get_articles_all_text(soup):
    pass


if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    base_url = 'https://habr.com'
    url = base_url + '/ru/all/'
    soup = get_soup(base_url, HEADERS)
