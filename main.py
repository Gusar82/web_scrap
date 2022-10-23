"""Задача 1: Необходимо парсить страницу со свежими статьями (https://habr.com/ru/all/) и выбирать те статьи,
   в которых встречается хотя бы одно из ключевых слов (эти слова определяем в начале скрипта).
   Поиск вести по всей доступной preview-информации (это информация, доступная непосредственно с текущей страницы).
   Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>.

   Задача 2: Улучшить скрипт так, чтобы он анализировал не только preview-информацию статьи,
   но и весь текст статьи целиком."""

from requests import get
import bs4
from header import HEADERS
from decorators import log, log_path
from pprint import pprint


def get_soup(url, header):
    responce = get(url, headers=header)
    text = responce.text
    return bs4.BeautifulSoup(text, features='html.parser')


def get_articles_preview(soup):
    class_ = 'tm-article-body tm-article-snippet__lead'
    # class_v2 = "article-formatted-body article-formatted-body article-formatted-body_version-2"
    # class_v1 = "article-formatted-body article-formatted-body article-formatted-body_version-1"
    previw = soup.find(class_=class_)
    # print(previw.get_text())
    return previw.get_text()


def search_keywords(text, keywords):
    # for keyword in keywords:
    #     if text.lower().find(keyword.lower()) != -1:
    #         return True
    # return False
    set_search = set(text.lower().split()) & set(keywords)
    return set_search

@log
@log_path(path=r"logs\date.log")
def get_date_articles(soup):
    time = soup.find('time')
    # print(time.attrs)
    return time['title']


@log
@log_path(path=r"logs\title.log")
def get_title_articles(soup):
    title = soup.find(class_="tm-article-snippet__title-link")
    # print(title.prettify())
    return title.span.text


def get_href_articles(soup, base_url):
    title = soup.find(class_="tm-article-snippet__title-link")
    return base_url+title['href']


def get_articles_all_text(soup):
    id_ = "post-content-body"
    xmlns_ = "http://www.w3.org/1999/xhtml"
    all_article = soup.find(id=id_).find(xmlns=xmlns_)
    return all_article.get_text()


def output_article(soup, base_url):
    """в формате: <дата> - <заголовок> - <ссылка>"""
    date = get_date_articles(soup)
    title = get_title_articles(soup)
    href = get_href_articles(soup, base_url)
    return f"<{date}> - <{title}> - <{href}>"



def main():
    KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'интеллект']
    base_url = 'https://habr.com'
    url = base_url + '/ru/all/'
    soup = get_soup(url, HEADERS)
    articles = soup.find_all('article')

    # Задача №1:
    print("Задача №1 : Поиск по preview", sep="\n")
    for article in articles:
        # pprint(article.prettify())
        text_article_preview = get_articles_preview(article)
        if search_keywords(text_article_preview, KEYWORDS):
            print(output_article(article, base_url))

    print("-----------------------------------------------")
    # Задача №2:
    print("Задача №2 : Поиск по всему тексту")
    for article in articles:
        href = get_href_articles(article, base_url)
        soup_article = get_soup(href, HEADERS)
        text_all_articles = get_articles_all_text(soup_article)
        if search_keywords(text_all_articles, KEYWORDS):
            print(output_article(article, base_url))


if __name__ == '__main__':
    main()
