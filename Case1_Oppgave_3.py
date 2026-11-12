def get_all_wares_in_stock(all_wares):
    dict_wares = {}

    for key, ware in all_wares.items():
        if is_ware_in_stock(ware):
            dict_wares[key] = ware

    return dict_wares

# Pre definert funksjon
def is_ware_in_stock(ware):
    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False