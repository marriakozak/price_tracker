import pandas as pd
import storage
import datetime as DT
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
    prices_df = prepare_prices_data()# load prices as data frame
    prices_df=prices_df.groupby(COL_PRODUCT_ID).tail(2) #group by products (by IDs)
    prices_df = prices_df.groupby(COL_PRODUCT_ID)[COL_PRICE].agg(["first","last"])
    prices_df = prices_df.rename(columns={"first": "prev"})
    loaded_products = storage.load_products()  # load productss
    products_df = pd.DataFrame(loaded_products)  # data frame from loaded product
    products_df = products_df[[COL_ID, COL_NAME]]
    products_df[COL_ID] = products_df[COL_ID].astype(int)
    merged_pd = pd.merge(products_df, prices_df, left_on="id", right_index=True)
    drops=merged_pd[merged_pd["last"] < merged_pd["prev"]]
    drops["drop"] = drops["prev"] - drops["last"]
    if drops.empty: print("No price drops.")
    else:
        print(drops)

def show_price_increases():
    prices_df = prepare_prices_data()  # load prices as data frame
    prices_df = prices_df.groupby(COL_PRODUCT_ID).tail(2)  # group by products (by IDs)
    prices_df = prices_df.groupby(COL_PRODUCT_ID)[COL_PRICE].agg(["first", "last"])
    prices_df = prices_df.rename(columns={"first": "prev"})
    loaded_products = storage.load_products()  # load productss
    products_df = pd.DataFrame(loaded_products)  # data frame from loaded product
    products_df = products_df[[COL_ID, COL_NAME]]
    products_df[COL_ID] = products_df[COL_ID].astype(int)
    merged_pd = pd.merge(products_df, prices_df, left_on="id", right_index=True)
    increases = merged_pd[merged_pd["last"] > merged_pd["prev"]]
    increases["increase"]=increases["last"]-increases["prev"]
    if increases.empty: print("No price increases.")
    else:
        print(increases)

def show_prices_below_target():
    prices_df = prepare_prices_data()  # load prices as data frame
    loaded_products = storage.load_products()  # load productss
    products_df = pd.DataFrame(loaded_products)  # data frame from loaded product
    products_df[COL_TARGET_PRICE] = products_df[COL_TARGET_PRICE].astype(float)
    products_df[COL_ID] = products_df[COL_ID].astype(int)
    last_prices_df=prices_df.groupby(COL_PRODUCT_ID)[COL_PRICE].last()
    merged_pd=pd.merge(products_df, last_prices_df, left_on="id", right_index=True)
    below_target_pd=merged_pd[merged_pd[COL_PRICE] < merged_pd[COL_TARGET_PRICE]]
    if below_target_pd.empty: print("No prices below target price.")
    else:
        print(below_target_pd)


def prepare_prices_data():
    loaded_history = storage.load_prices()  # load prices
    prices_df = pd.DataFrame(loaded_history)  # data frame from loaded prices
    prices_df[COL_PRICE] = prices_df[COL_PRICE].astype(float)
    prices_df[COL_PRODUCT_ID] = prices_df[COL_PRODUCT_ID].astype(int)
    prices_df[COL_TIME] = pd.to_datetime(prices_df[COL_TIME])
    prices_df=prices_df.sort_values(by=COL_TIME,ascending=True)
   # print(prices_df[COL_TIME].head())
    return prices_df


def price_drops_within_period(number_of_days=7):
    today = pd.Timestamp.today().normalize()
    prices_data=prepare_prices_data()
    filtered_prices=prices_data[prices_data[COL_TIME]>(today - DT.timedelta(days=number_of_days))]
    filtered_prices=filtered_prices.groupby([COL_PRODUCT_ID])[COL_PRICE].agg(["first", "last"])
    drops = filtered_prices[filtered_prices["first"] > filtered_prices["last"]]
    drops["drop"] = drops["first"] - drops["last"]
    if drops.empty: print(f"No price drops within last {number_of_days}.")
    else:
        print(f"There were {len(drops)} drops within last {number_of_days}.")
        print(drops)

def average_price_changes():
    prices_df = prepare_prices_data()
    prices_df = prices_df.groupby(COL_PRODUCT_ID)[COL_PRICE].agg(["first", "last", "count"])
    prices_df["total_change"]=prices_df["last"]-prices_df["first"]
    count_minus_one = (prices_df["count"] - 1).astype(float)
    prices_df["avg_change"] = prices_df["total_change"] / count_minus_one.replace(0, float("nan"))
    if prices_df.empty: print("No price changes.")
    else:
        print(prices_df)

def prices_at_lowest():
    prices_df = prepare_prices_data()
    prices_df = prices_df.groupby(COL_PRODUCT_ID)[COL_PRICE].agg(["last", "min"])
    loaded_products = storage.load_products()
    products_df = pd.DataFrame(loaded_products)  # data frame from loaded product
    products_df[COL_TARGET_PRICE] = products_df[COL_TARGET_PRICE].astype(float)
    products_df[COL_ID] = products_df[COL_ID].astype(int)
    merged_pd = pd.merge(products_df, prices_df, left_on="id", right_index=True)
    at_lowest_pd = merged_pd[merged_pd["last"] == merged_pd["min"]]
    if at_lowest_pd.empty: print("No prices at lowest.")
    else:
        print(at_lowest_pd)

def print_stats():
    print("=" * 60)
    print("PRICE STATISTICS")
    print("=" * 60)

    print("\n--- PRICE DROPS (last vs previous check) ---")
    print("Products whose latest price is lower than the previous one:")
    show_price_drops()

    print("\n--- PRICE INCREASES (last vs previous check) ---")
    print("Products whose latest price is higher than the previous one:")
    show_price_increases()

    print("\n--- DROPS WITHIN LAST 7 DAYS ---")
    print("Products whose price dropped compared to the start of the period:")
    price_drops_within_period(7)

    print("\n--- BELOW TARGET PRICE ---")
    print("Products currently cheaper than their target price:")
    show_prices_below_target()

    print("\n--- AVERAGE PRICE CHANGE PER CHECK ---")
    print("Average change between consecutive checks, per product:")
    average_price_changes()

    print("\n--- AT LOWEST PRICE EVER ---")
    print("Products currently at their historical minimum:")
    prices_at_lowest()

    print("\n" + "=" * 60)

#show_price_drops()
#show_price_increases()
#price_drops_last_week()
#show_prices_below_target()
#average_price_changes()
#prices_at_lowest()

