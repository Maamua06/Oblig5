from datetime import date

def next_eu_control(car):
    year = car["year"]

    next_eu = year + 2

    return date(next_eu, car["month"],1)