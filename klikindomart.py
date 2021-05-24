import pprint

import requests
from bs4 import BeautifulSoup

from config import settings
from schema import ItemDetail
from utils import clean_price

base_url = settings.KLIKINDOMART_BASE_URL
promo_url = settings.KLIKINDOMART_PROMO_URL

promo_full_url = base_url + promo_url

req = requests.get(promo_full_url).text
parser = BeautifulSoup(req, 'html.parser')

box = parser.find('div', {'class': 'box-item clearfix'})

item_list = []

for item in box.find_all('div', {'class': 'item'}):
    wrp_content = item.find('div', {'class': 'wrp-content'})

    product_link = item.find('a').get('href')
    product_name = wrp_content.find('div', {'class': 'title'}).text.strip()
    raw_product_discount = wrp_content.find('span', {'class': 'strikeout disc-price'})
    product_discount = clean_price(raw_product_discount.text.split('\n')[0]) if raw_product_discount else ''
    product_price = clean_price(wrp_content.find('span', {'class': 'normal price-value'}).text.strip())
    product_from = wrp_content.find('span', {'class': 'sendbyProduct'}).text.strip()

    product_full_url = base_url + product_link

    data = ItemDetail(product_name=product_name, product_link=product_full_url,
                      product_discount_price=product_discount, product_price=product_price,
                      product_from=product_from).dict()

    item_list.append(data)

pprint.pprint(item_list)

# for pagination all promo
# get_pagination = parser.find('select', {'class': 'form-control pagelist'})
# get_length_pagination = len(get_pagination.find_all('option'))
