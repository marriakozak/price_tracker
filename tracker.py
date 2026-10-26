import storage
import notifier
import scraper
from config import PRODUCTS_FILE, PRICES_FILE, COL_ID, COL_NAME,COL_PRODUCT_URL, COL_DESCRIPTION, COL_TARGET_PRICE, COL_PRODUCT_ID, COL_PRICE, COL_TIME


def check_product(product):
    html=scraper.fetch_html(product.get(COL_PRODUCT_URL))
    if html is None:
        print("Html not fetched")
        return False
    current_price=scraper.extract_price(html)
    if current_price is None:
        print("Price not found")
        return False
    notifier.notify(product, current_price)
    storage.add_price_record(product.get(COL_ID), current_price)
    return current_price

def check_all_products(products):
    for product in products:
        check_product(product)
