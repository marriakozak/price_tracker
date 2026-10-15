#defining varianles with file names
PRODUCTS_FILE = "products.csv"
PRICES_FILE = "prices.csv"

#defining variables with column names for file with product list
COL_ID = "id"
COL_NAME = "name"
COL_URL = "url"
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
}