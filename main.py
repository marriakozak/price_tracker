from socket import EAGAIN
from soupsieve.css_types import Null
from config import PRODUCTS_FILE, PRICES_FILE, COL_ID, COL_NAME, COL_PRODUCT_URL, COL_DESCRIPTION,COL_TARGET_PRICE, COL_PRODUCT_ID, COL_PRICE, COL_TIME
#from storage import init_files, add_price_record, load_products
import storage
import scraper

storage.init_files()
'''
#---------testing scraping functions------
shoes_url= scraper.build_search_url("https://mmsport.pl","Buty biegowe męskie Under Armour Rogue 6")
#shoes_url=scraper.find_product_url(scraper.fetch_html("https://mmsport.pl/search.php?text=Under+Armour+Rogue+6"),"Under Armour Rogue 6")
print(shoes_url)
product_url= scraper.find_product_url(scraper.fetch_html(shoes_url), "Buty biegowe męskie Under Armour Rogue 6")

price_text= scraper.extract_price(scraper.fetch_html(product_url))
print(price_text)
'''

products = storage.load_products() #to load all products from the file
print(f"Length of products: {len(products)}")
# function that will display menu

def display_menu():
    menu_text = (
        "Hello, I'm your price tracker. Put one of the following numbers to continue: /n "
        "1 - list the current products /n "# i don't have this option yet unless im fine with the whole dictionary
        "2 - add product to the list /n "  
        "3 - remove product from the list /n "
        "4 - set the frequency of price checker /n "
        "5 - "  # I will see if there will be one function to run statistics or more
        "0 - exit program"
    )
    print(menu_text)
    selected_option = int(input("select option: "))
    return selected_option

#---------dealing with user--------

while True:
    selected_option = display_menu()
    if selected_option==1: #printing list of products with all the information from the file - may be useful to write code to get the product names only or names and shop url
        print(products)
    elif selected_option == 2: #to add new product to the list, including checking the product url
        #products = storage.load_products() #to load all products from the file
        max_id=0 #finding max product id to identify what should be new id
        for product in products:
            if product["id"] > max_id:
                max_id = product["id"]
        product_name=input("Provide product name: ") #asking user for product name
        shop_url=input("Provide shop url: ") #asking user for shop url
        product_url=scraper.find_product_url(scraper.fetch_html(scraper.build_search_url(shop_url, product_name)),product_name) #finding product url
        product_description=input("Provide product description: ") #asking user for product description
        product_target_price=float(input("Provide product target price: ")) #asking user for target price and converting it to float
        #product_price=scraper.extract_price(scraper.fetch_html())
        storage.add_product(products,max_id+1,product_url,product_name,product_description, product_target_price) #adding new product to products list
    elif selected_option == 3: #removing product from the list
        #products = storage.load_products()  # to load all products from the file
        product_to_remove=input("Provide name of the product to be removed: ")
        storage.remove_product(storage.get_product_id_by_name(products,product_to_remove))
        print(f"({product_to_remove} has been removed from the list.)")
    elif selected_option == 4:
        frequency =input("Provide frequency of price checker: ")
    elif selected_option ==5:
        print("Stats: ")
    elif selected_option== 0:
        storage.save_products(products)
        break
    else:
        print("Incorrect value. Please provide the correct number: ")


