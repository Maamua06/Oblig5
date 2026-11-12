from Case1_Oppgave_3 import is_ware_in_stock
from Case1_Oppgave_4 import is_number_of_ware_in_stock

def add_number_or_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware = 1):
    if is_number_of_ware_in_stock(ware, number_of_ware):
        return shopping_cart.update({ware_key: number_of_ware})
    elif is_ware_in_stock(ware):
        print(f"Det er kun {ware["number_in_stock"]} av {number_of_ware} på lager")
        return shopping_cart.update({ware_key: ware["number_in_stock"]})
    else:
        print(f"{ware_key} er ikke på lager")
        return None