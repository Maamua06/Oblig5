# La til parameteret car_name sånn at det kan være key valuen i dictionary car_register
def create_car(car_register,car_name, brand, model, price, year, month, new, km):
     car_dict = {"brand" : brand,
                  "model": model,
                  "price": price,
                  "year": year,
                  "month": month,
                  "new": new,
                  "km": km}

     return car_register.update({car_name : car_dict})