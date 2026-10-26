from enum import nonmember

import requests
from bs4 import BeautifulSoup
from config import HEADERS
from urllib.parse import quote
#import mechanicalsoup
import time

# works for now for "https://mmsport.pl/"
'''
browser.session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9"
}) #to hide that this is a bot
'''
def build_search_url(shop_url, product_name):
    #if shop_url == "https://sportofino.com":

        #shop_url = shop_url.rstrip('/') + "/catalogsearch/result/?q=" + quote(product_name)

    shop_url = shop_url+"/search.php?text="+product_name.replace(" ", "+")
    return shop_url

def fetch_html(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)

        if response.status_code == 200:
            print("HTML dowloaded successfully.")
            return response.text
        else:
            print(f"Website response error: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Connection error: {e}")
        return None

def find_product_url(html, product_name):
    if html is None:
        return None

    soup = BeautifulSoup(html, "html.parser")
    product_elements = soup.select("a")
    #name_lower = product_name.lower()
    for element in product_elements:
        '''
        candidates = [
            element.get_text().strip().lower(),
            (element.get("title") or "").lower(),
            (element.get("alt") or "").lower(),
        ]
        if any(name_lower in c for c in candidates if c):
            return element.get("href")'''
        text = element.get_text().strip().lower()
        #print(repr(text))
        if product_name.lower() in element.get_text().strip().lower():
            return element.get("href")
    print("Product not found")
    return None


def extract_price(html):
    if html==None:
        return None
    soup = BeautifulSoup(html, "html.parser")
    price_element = soup.select_one("#projector_price_value")
    price = price_element.get("data-price")
    return float(price)
