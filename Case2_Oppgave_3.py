from datetime import date

def get_car_age(car):
    car_year = car["year"]

    today_date = str(date.today())
    split_string_list = today_date.split("-")
    year_today = int(split_string_list[0])

    age = year_today - car_year

    if age == 0:
        return 1

    return age