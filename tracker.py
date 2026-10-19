from notifier import notify
from scraper import fetch_html, extract_price
from storage import add_price_record

import config


def check_product(product):
    html=fetch_html(product.get("product_url"))
    if html is None:
        print("Html not fetched")
        return False
    current_price=extract_price(html)
    if current_price is None:
        print("Price not found")
        return False
    notify(product, current_price)
    add_price_record(product.get("id"), current_price)
    return current_price

def check_all_products(products):
    for product in products:
        check_product(product)
