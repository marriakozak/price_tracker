import pandas as pd
import storage
from config import PRODUCTS_FILE, PRICES_FILE, COL_ID, COL_NAME,COL_PRODUCT_URL, COL_DESCRIPTION, COL_TARGET_PRICE, COL_PRODUCT_ID, COL_PRICE, COL_TIME

def show_history(product_id=None):
    loaded_history=storage.load_prices(product_id)# load prices
    history_df=pd.DataFrame(loaded_history)# data frame from loaded prices
    history_df=history_df.sort_values(by=COL_TIME,ascending=True) #sorting by time (though generaly it should be sorted)
    print(history_df) #printing the history

def show_all_products(products):
    loaded_products=storage.load_products(products)
    products_df=pd.DataFrame(loaded_products)
    print(products_df)

def show_price_drops():
    loaded_history = storage.load_prices()  # load prices
    prices_df = pd.DataFrame(loaded_history)# data frame from loaded prices
    prices_df=prices_df.sort_values(by=COL_TIME,ascending=True)#make sure the time is in order by sorting
    last=prices_df.groupby(COL_PRODUCT_ID)[COL_PRICE].last() #group by products (by IDs)
    prev=prices_df.groupby(COL_PRODUCT_ID)[COL_PRICE].nth(-2)
    drops=last[last<prev]
    print(drops)


def show_price_increases():
    loaded_history = storage.load_prices()  # load prices
    prices_df = pd.DataFrame(loaded_history)# data frame from loaded prices
    prices_df=prices_df.sort_values(by=COL_TIME,ascending=True)
    last=prices_df.groupby(COL_PRODUCT_ID)[COL_PRICE].last()
    prev=prices_df.groupby(COL_PRODUCT_ID)[COL_PRICE].nth(-2)
    increases=last[last>prev]
    print(increases)