import time
from tracker import check_all_products, check_product
from storage import load_products

def run_scheduler(products, interval_minutes, max_runs=None): #there is default none option if we want the program to run without limited number of iterations    counter=0
    counter=0
    while counter<max_runs or max_runs==None:
        check_all_products(products)
        time.sleep(interval_minutes*60)
        counter+=1
