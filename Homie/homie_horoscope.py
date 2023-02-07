from bs4 import BeautifulSoup
import requests
from googletrans import Translator


def get_horoscopo(signo):

    number = {
        'aries': 1,
        'tauro': 2,
        'géminis': 3,
        'cáncer': 4,
        'leo': 5,
        'virgo': 6,
        'libra': 7,
        'escorpio': 8,
        'sagitario': 9,
        'capricornio': 10,
        'acuario': 11,
        'piscis': 12
    }

    website = f'https://www.horoscope.com/us/horoscopes/' \
              f'general/horoscope-general-daily-today.aspx?sign={number[signo]}'
    res = requests.get(website)
    content = res.text

    soup = BeautifulSoup(content, 'lxml')
    horoscope = soup.find('div', class_='main-horoscope').find('p').get_text().split(' - ')[1]
    translator = Translator(service_urls=['translate.googleapis.com'])
    return translator.translate(horoscope, dest='es').text
