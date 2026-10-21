#defining varianles with file names
PRODUCTS_FILE = "products.csv"
PRICES_FILE = "prices.csv"

#defining variables with column names for file with product list
COL_ID = "id"
COL_NAME = "name"
COL_PRODUCT_URL = "url"
COL_DESCRIPTION= "description"
COL_TARGET_PRICE= "target price"

#defining variables with column names for file with prices
COL_PRODUCT_ID = "product id"
COL_PRICE = "price"
COL_TIME = "time"

#variable for web scrapping
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/155.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,image/apng,*/*;q=0.8"
    ),
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://sportofino.com/",
}