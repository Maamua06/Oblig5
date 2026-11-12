def rent_car_monthly_price(car):
    price = car["price"]

    yearly_fee = price * 40 / 100
    monthly_fee = round(yearly_fee / 12, 2)

    if is_new(car):
        return monthly_fee + 1000

    return monthly_fee


def is_new(car):
    return car["new"]