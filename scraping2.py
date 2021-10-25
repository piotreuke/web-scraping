import requests
from bs4 import BeautifulSoup
import time

class GetData:

    def __init__(self, url):
        self.url = url
        self.page_source = self.get_data()

    def get_data(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            return r.text
        else: return None

    def show_page_source(self):

        print(self.page_source)


class ParseData:
    def __init__(self, page_source):
        self.page_source = page_source

    def parse(self):
        soup = BeautifulSoup(self.page_source, 'html.parser')
        div_element = soup.find('div', {'class' : 'priceValue'})
        text = div_element.text
        return text

data = GetData(url='https://coinmarketcap.com/pl/currencies/bitcoin/')
parser = ParseData(page_source=data.page_source)
output = parser.parse()
print(output)


plik = open('bitcoin.txt', 'w')

plik.write(output)


plik.close()
