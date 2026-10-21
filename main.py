from socket import EAGAIN

from soupsieve.css_types import Null
from config import PRODUCTS_FILE, PRICES_FILE, COL_ID, COL_NAME, COL_PRODUCT_URL, COL_DESCRIPTION,COL_TARGET_PRICE, COL_PRODUCT_ID, COL_PRICE, COL_TIME
from storage import init_files, add_price_record
import scraper

init_files()
'''
#---------testing scraping functions------
shoes_url= scraper.build_search_url("https://mmsport.pl","Buty biegowe męskie Under Armour Rogue 6")
#shoes_url=scraper.find_product_url(scraper.fetch_html("https://mmsport.pl/search.php?text=Under+Armour+Rogue+6"),"Under Armour Rogue 6")
print(shoes_url)
product_url= scraper.find_product_url(scraper.fetch_html(shoes_url), "Buty biegowe męskie Under Armour Rogue 6")

price_text= scraper.extract_price(scraper.fetch_html(product_url))
print(price_text)
'''

# to finish - text be displayed when running the program by a function that will display menu
menu_text =(
    "Hello, I'm your price tracker. Put one of the following numbers to continue: /n"
    " 0 - to display the menu again /n"
    "1 - list the current products /n" # i don't have this option yet unless im fine with the whole dictionary
    "2 - add product to the list /n"
    "3 - remove product from the list /n"
    "4 - set the frequency of price checker /n"
    "5 - "
)
