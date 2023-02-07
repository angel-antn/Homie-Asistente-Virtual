from bs4 import BeautifulSoup
import requests


def get_wiki(palabra):
    website = f'https://es.wikipedia.org/wiki/{palabra.title().replace(" ", "_")}'
    res = requests.get(website)
    content = res.text

    soup = BeautifulSoup(content, 'lxml')
    res = soup.find('div', id='mw-content-text').find('div', class_='mw-parser-output').find_all('p', recursive=False)
    for i in res:

        definition = i.get_text()
        if definition.strip() != '':
            definition = definition.split(".")[0]
            aux = ''
            delete = False
            delete_2 = False
            for j in definition:

                if j == '(':
                    delete = True
                elif j == '[':
                    delete_2 = True

                if not delete and not delete_2:
                    aux += j

                if delete and j == ")":
                    delete = False
                elif delete_2 and j == "]":
                    delete_2 = False

            if aux != '':
                return f'esto fue lo que conseguí sobre {palabra}. {aux}'
