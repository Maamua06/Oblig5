def calculate_shopping_cart_price(shopping_cart, all_wares, tax = 25.0):
    list_item = shopping_cart.keys()
    total_price = 0

    for item in list_item:
        price = all_wares[item]["price"]
        price_with_tax = price + (price * tax / 100)
        total_price += price_with_tax

    return total_price