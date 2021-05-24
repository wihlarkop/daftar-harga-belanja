import requests
from bs4 import BeautifulSoup

from config import settings
from schema import ProductDetail, ProductPrice
from utils import clean_price


def get_promo_url():
    request_promo_url = requests.get(settings.KLIKINDOMART_BASE_URL).text
    parser_promo_url = BeautifulSoup(request_promo_url, 'html.parser')

    promo = parser_promo_url.find('div', {'class': 'seemore col-xs-6 text-right'})
    url = promo.find('a').get('href')

    return url


def get_total_page():
    base_url = get_promo_url()

    full_url = f'{base_url}{settings.KLIKINDOMART_PARAMS}'

    requests_page = requests.get(full_url).text

    page = BeautifulSoup(requests_page, 'html.parser')

    get_page = page.find("select", {"class": "form-control pagelist"})

    length_page = len(get_page.find_all('option'))

    return length_page


def get_product_promo_list():
    products = []

    length_page = get_total_page()

    for page in range(0, length_page):
        base_url = get_promo_url()

        full_url_data = f'{base_url}{settings.KLIKINDOMART_PARAMS}{settings.KLIKINDOMART_PARAM_PAGE}{page + 1}'

        req = requests.get(full_url_data).text

        parser = BeautifulSoup(req, 'html.parser')

        box = parser.find('div', {'class': 'box-item clearfix'})

        for item in box.find_all('div', {'class': 'item'}):
            wrp_content = item.find('div', {'class': 'wrp-content'})

            product_link = item.find('a').get('href')
            product_name = wrp_content.find('div', {'class': 'title'}).text.strip()
            raw_product_discount = wrp_content.find('span', {'class': 'strikeout disc-price'})
            product_discount = clean_price(raw_product_discount.text.split('\n')[0]) if raw_product_discount else ''
            product_price = clean_price(wrp_content.find('span', {'class': 'normal price-value'}).text.strip())
            product_from = wrp_content.find('span', {'class': 'sendbyProduct'}).text.strip()

            product_full_url = base_url + product_link

            price = ProductPrice(product_price=product_price, product_discount_price=product_discount)

            product_detail = ProductDetail(product_name=product_name, product_link=product_full_url, price=price,
                                           product_from=product_from).dict()

            products.append(product_detail)

    return products
