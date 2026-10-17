from config import PRODUCTS_FILE, PRICES_FILE, COL_ID, COL_NAME, COL_PRODUCT_URL, COL_DESCRIPTION,COL_TARGET_PRICE, COL_PRODUCT_ID, COL_PRICE, COL_TIME
from storage import init_files
import scraper

init_files()
print("It's working so far!")

#---------testing scraping functions------
shoes_url= scraper.build_search_url("https://mmsport.pl","Under Armour Rogue 6")
#shoes_url=scraper.find_product_url(scraper.fetch_html("https://mmsport.pl/search.php?text=Under+Armour+Rogue+6"),"Under Armour Rogue 6")
print(shoes_url)
product_url= scraper.find_product_url(scraper.fetch_html(shoes_url), "Under Armour Rogue 6")

price_text= scraper.extract_price(scraper.fetch_html(product_url))
print(price_text)