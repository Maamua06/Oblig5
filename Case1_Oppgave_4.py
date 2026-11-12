def is_number_of_ware_in_stock(ware, number_of_ware):
    if ware["number_in_stock"] >= number_of_ware:
        return True
    else:
        return False