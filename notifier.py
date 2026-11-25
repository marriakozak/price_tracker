from config import PRODUCTS_FILE, PRICES_FILE, COL_ID, COL_NAME,COL_PRODUCT_URL, COL_DESCRIPTION, COL_TARGET_PRICE, COL_PRODUCT_ID, COL_PRICE, COL_TIME
import storage

def notify(product, current_price):
    last_price = storage.get_last_price(product[COL_ID])

    if last_price is None:
        return
    if float(last_price)>float(current_price):
        print(f'Check out {product["name"]}. The price dropped!')
    if float(product.get(COL_TARGET_PRICE))>=float(current_price):
        print(f'Check out {product["name"]}. It is within your budget now!')