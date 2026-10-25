import csv
import os.path
from datetime import datetime
from config import PRODUCTS_FILE, PRICES_FILE, COL_ID, COL_NAME,COL_PRODUCT_URL, COL_DESCRIPTION, COL_TARGET_PRICE, COL_PRODUCT_ID, COL_PRICE, COL_TIME


#to create files if they don't exist yet
def init_files():
    if not os.path.exists("data"): #to create a folder if it doesn't exist yet
        os.makedirs("data")
    if not os.path.exists(PRODUCTS_FILE): # to create a file with list of products
        try:
            with open(PRODUCTS_FILE, "w", newline="") as f:
                writer = csv.DictWriter(f)
                writer.writerow([COL_ID, COL_NAME, COL_PRODUCT_URL, COL_DESCRIPTION, COL_TARGET_PRICE])
        except IOError:
            print("Something went wrong when creating products file")
        if not os.path.exists(PRICES_FILE):  # to create a file with prices
            try:
                with open(PRICES_FILE, "w", newline="") as fi:
                    writer = csv.DictWriter(fi)
                    writer.writerow([COL_PRODUCT_ID, COL_PRICE, COL_TIME])
            except IOError:
                print("Something went wrong when creating prices file")

        # wczytaj listę słowników z CSV (uwaga: obsłuż przypadek, gdy plik nie istnieje)

def load_products():
    try:
        with open(PRODUCTS_FILE, 'r') as f:
            reader=csv.DictReader(f)
            products=list(reader)
            return products
    except FileNotFoundError:
        print("File does not exist") # runs if the file doesn't exist
    except PermissionError:
        print("No permission to open file")  # access denied
    except IOError:
        print("Something went wrong")  # general file error

def save_products(products):
    try:
        with open(PRODUCTS_FILE, 'w', encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f,[COL_ID, COL_NAME, COL_PRODUCT_URL, COL_DESCRIPTION, COL_TARGET_PRICE])
            writer.writeheader()
            writer.writerows(products)
    except FileNotFoundError:
        print("File does not exist") # runs if the file doesn't exist
    except PermissionError:
        print("No permission to open file")  # access denied
    except IOError:
        print("Something went wrong")  # general file error

#this function adds a new product to products list variable in the main file, which was loaded from the products file
def add_product(products, id, name, url, description, target_price):
    new_id=max((p[COL_ID] for p in products),default=0)+1
    products.append ({COL_ID: id, COL_NAME: name, COL_PRODUCT_URL: url, COL_DESCRIPTION: description, COL_TARGET_PRICE: target_price})

def remove_product(products,product_id): #— usuń z listy i zapisz
    products=[p for p in products if p[COL_ID] != product_id] #using list comprehension to create a new products list without the product to be removed
    return products

def get_product_id_by_name(products, name):
    for p in products:
        if p[COL_NAME] == name:
            return p[COL_ID]

def get_product_by_id(product_id):
    for p in products:
        if p[COL_ID] == product_id:
            searched_product = p
    return searched_product

def add_price_record(product_id, price):
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(PRICES_FILE, 'a',encoding='utf-8',newline="") as f:
            writer = csv.DictWriter(f,[COL_PRODUCT_ID, COL_PRICE, COL_TIME])
            writer.writerow([product_id, price,date_str])
    except OSError as e:
        print(f"Error while writing to the file: {e}")

