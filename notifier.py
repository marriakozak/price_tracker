

def notify(product, current_price):
    if product.get("target_price")>=current_price:
        print(f"Check out {product.get("name")}. It is within your budget now!")