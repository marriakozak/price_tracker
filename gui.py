import tkinter as tk
from tkinter import ttk
import storage
from config import COL_ID, COL_NAME, COL_PRODUCT_URL, COL_TARGET_PRICE

def main():
    #-------------------uploading the data-----------------------------------
    storage.init_files() #initializing the products and prices files
    products = storage.load_products()  # to load all products from the file

    #-------------------window creation, title, geometry----------------------
    window = tk.Tk() # creating the window
    window.title("Price Tracker") #naming the window
    window.geometry("900x500") # setting up the size of the window

    #-------------------treeview----------------------------------------------
    tree = ttk.Treeview(
        window,
        columns=(COL_ID, COL_NAME, COL_PRODUCT_URL, COL_TARGET_PRICE),
        show="headings",
    )

    #headers and headerss alignment to center
    tree.heading(COL_ID, text="ID", anchor="center")
    tree.heading(COL_NAME, text="Name", anchor="center")
    tree.heading(COL_PRODUCT_URL, text="URL", anchor="center")
    tree.heading(COL_TARGET_PRICE, text="Target", anchor="center")

    #column width and values alignment to center or west
    tree.column(COL_ID, width=50, anchor="center")
    tree.column(COL_NAME, width=200, anchor="w")
    tree.column(COL_PRODUCT_URL, width=300, anchor="w")
    tree.column(COL_TARGET_PRICE, width=80, anchor="center")

    tree.pack(fill="both", expand=True) #table is filling in both directions and taking whole free psace in the window

    #-------------------- refresh window function to clean and upload the window-----------------------
    def refresh_tree():
        # clearing rows in the table
        for item in tree.get_children():
            tree.delete(item)

        # uploading products data
        for product in products:
            tree.insert("", "end", values=(product[COL_ID], product[COL_NAME], product[COL_PRODUCT_URL], product[COL_TARGET_PRICE]))

    # calling the refresh function
    refresh_tree()

    window.mainloop()

main()






