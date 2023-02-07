from bs4 import BeautifulSoup
import requests


def get_dolar_bcv():
    website = 'https://www.bcv.org.ve'
    res = requests.get(website, verify=False)
    content = res.text

    soup = BeautifulSoup(content, 'lxml')
    res = float(soup.find('div', id='dolar').find('strong').get_text().replace(',', '.'))
    return 'Según el banco central de venezuela, el dólar se encuentra en %.2f bolívares' % res


def get_euro_bcv():
    website = 'https://www.bcv.org.ve'
    res = requests.get(website, verify=False)
    content = res.text

    soup = BeautifulSoup(content, 'lxml')
    res = float(soup.find('div', id='euro').find('strong').get_text().replace(',', '.'))
    return 'Según el banco central de venezuela, el euro se encuentra en %.2f bolívares' % res


def calc_dolar(dolares):
    website = 'https://www.bcv.org.ve'
    res = requests.get(website, verify=False)
    content = res.text

    soup = BeautifulSoup(content, 'lxml')
    res = float(soup.find('div', id='dolar').find('strong').get_text().replace(',', '.'))
    res *= dolares
    return f'Según el banco central de venezuela, {"%.2f" % dolares} dólares equivalen a {"% .2f" % res} bolívares'


def calc_euro(euros):
    website = 'https://www.bcv.org.ve'
    res = requests.get(website, verify=False)
    content = res.text

    soup = BeautifulSoup(content, 'lxml')
    res = float(soup.find('div', id='euro').find('strong').get_text().replace(',', '.'))
    res *= euros
    return f'Según el banco central de venezuela, {"%.2f" % euros} euros equivalen a {"% .2f" % res} bolívares'
