from Case2_Oppgave_3 import get_car_age

def calculate_total_price(car):
    if car["new"]:
        return car["price"] + 10783

    return car["price"] + calculate_fee(car)


# Funskjon som regner ut avgift basert på alder til bilen
def calculate_fee(car):
    age = get_car_age(car)
    match age:
        case 1 if age <= 3:
            return 6681
        case 2 if age <= 11:
            return 4034
        case 3 if age <= 29:
            return 1729
        case 4 if age >= 30:
            return 0
        case _:
            return 0