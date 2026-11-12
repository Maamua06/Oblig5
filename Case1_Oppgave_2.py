def calculate_average_ware_rating(ware):
    try:
        rating_list = ware["ratings"]
        rating_sum = 0
        total_ratings = 0

        for rating in rating_list:
            rating_sum += rating
            total_ratings += 1

        return round(rating_sum / total_ratings, 1)
    except ZeroDivisionError:
        print("Denne varen har ingen rating")