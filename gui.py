import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import storage
import scraper
import stats
import tracker
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

    #----------------------button frame-------------------------------------------------
    button_frame = tk.Frame(window) #creating frame
    button_frame.pack(fill="x", pady=5) #frame settings

    #refresh button------------------------------------
    refresh_button = tk.Button(button_frame, text="Refresh products", command=refresh_tree)
    refresh_button.pack(side="left", padx=5)

    #close button--------------------------------------
    close_button = tk.Button(button_frame, text="Close window", command=window.destroy)
    close_button.pack(side="right", padx=5)

    #remove product button-----------------------------

    def remove_selected():
        nonlocal products #I'm not modifying local variable
        selected = tree.selection()  # list of IDs of selected rows
        if not selected:
            messagebox.showinfo("No rows to be removed selected ", "Select product to be removed.")
            return

        item = selected[0]  # we take first select item
        values = tree.item(item, "values")
        product_id = int(values[0]) #we select ID column

        # confirmation from user that they want to remove
        if not messagebox.askyesno("Confrim", f"Do you want to remove product number {product_id}?"):
            return

        # remove and save
        products=storage.remove_product(products, product_id)
        storage.save_products(products)
        # refresh the table
        refresh_tree()

    #remove button
    remove_button = tk.Button(button_frame, text="Remove selected", command=remove_selected)
    remove_button.pack(side="left", padx=5)

    #---------------------------------adding products-------------------------------------------

    #adding function
    def add_product_dialog():
        dialog = tk.Toplevel(window)
        dialog.title("Add product")
        dialog.geometry("400x350")

        # fields
        tk.Label(dialog, text="Product name:").pack(pady=(10, 0))
        name_entry = tk.Entry(dialog, width=40)
        name_entry.pack()


        tk.Label(dialog, text="Shop URL:").pack(pady=(10, 0))
        shop_url_entry = tk.Entry(dialog, width=40)
        shop_url_entry.pack()

        tk.Label(dialog, text="Description:").pack(pady=(10, 0))
        desc_entry = tk.Entry(dialog, width=40)
        desc_entry.pack()

        tk.Label(dialog, text="Target price:").pack(pady=(10, 0))
        target_entry = tk.Entry(dialog, width=40)
        target_entry.pack()

        def save():
            nonlocal products  # to access non local products variable
            name = name_entry.get().strip()
            url = shop_url_entry.get().strip()
            description = desc_entry.get().strip()
            target_str = target_entry.get().strip()

            # validating
            if not name or not url:
                messagebox.showinfo("Error", "Name and URL are required.")
                return

            try:
                target = float(target_str)
            except ValueError:
                messagebox.showinfo("Error", "Target price must be a number.")
                return

            # --- SCRAPER: find product URL ---
            try:
                search_url = scraper.build_search_url(url, name)
                html = scraper.fetch_html(search_url)
                product_url = scraper.find_product_url(html, name)
            except Exception as e:
                messagebox.showinfo("Error", f"Scraper error: {e}")
                return
            if product_url is None:
                messagebox.showinfo("Error", "Product not found on the shop page.")
                return

            # add product
            products = storage.add_product(products, name, product_url, description, target)

            # refresh and save
            refresh_tree()
            dialog.destroy()
        pass

        def cancel():
            dialog.destroy()

        tk.Button(dialog, text="Save", command=save).pack(side="left", padx=10, pady=15)
        tk.Button(dialog, text="Cancel", command=cancel).pack(side="right", padx=10, pady=15)

    # add button
    add_button = tk.Button(button_frame, text="Add product", command=add_product_dialog)
    add_button.pack(side="left", padx=5)


    #--------------------------check all products------------------------
    def check_all():
        if not products:
            messagebox.showinfo("No products", "There are no products to check.")
            return

        try:
            tracker.check_all_products(products)
        except Exception as e:
            messagebox.showinfo("Error", f"Error while checking prices: {e}")
            return

        refresh_tree()
        messagebox.showinfo("Done", "All products checked.")

    #check all button
    check_button = tk.Button(button_frame, text="Check prices", command=check_all)
    check_button.pack(side="left", padx=5)



    window.mainloop()

main()






