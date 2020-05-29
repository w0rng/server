from hashlib import md5
import requests
from bs4 import BeautifulSoup as Soup


def generate_hash(s):
    return {
        'hash': md5(s.encode()).hexdigest()[:5]
    }


def get_current_week_evenness():
    soup = Soup(requests.get('https://timetable.pallada.sibsau.ru/timetable/group/5047').text, 'html.parser')
    even_week = str(soup.select('#week_2_tab'))
    return 'сегодня' in even_week
