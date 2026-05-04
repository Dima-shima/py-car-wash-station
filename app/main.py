from decimal import Decimal, ROUND_HALF_UP


class Car:
    def __init__(self, comfort_class, clean_mark, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings


    def serve_cars(self, car_list):
        income = 0
        for car in car_list:
            dif_clean = ws.clean_power - car.clean_mark
            rating_distance = ws.average_rating / ws.distance_from_city_center
            income_car = car.comfort_class * dif_clean * rating_distance
            if car.clean_mark < ws.clean_power:
                income += income_car
                car.clean_mark = ws.clean_power
        income = Decimal(income)
        return income.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        # return round(income, 1)


    def calculate_washing_price(self, car):
        dif_clean = ws.clean_power - car.clean_mark
        rating_distance = ws.average_rating / ws.distance_from_city_center
        income_car = car.comfort_class * dif_clean * rating_distance
        # income_car = Decimal(income_car)
        # return income_car.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        return round(income_car, 1)


    def wash_single_car(self, car):
        if car.clean_mark < ws.clean_power:
            car.clean_mark = ws.clean_power


    def rate_service(self, rate):
        old_rates = ws.average_rating * ws.count_of_ratings
        new_count = ws.count_of_ratings + 1
        new_rates = (old_rates + rate) / new_count
        new_rates = Decimal(new_rates)
        ws.average_rating = new_rates.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        ws.count_of_ratings = new_count
        return new_rates.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        # return round(new_rates, 1)


# ws = CarWashStation(2, 9, 3.8, 7)
# ws = CarWashStation(6, 8, 4.4, 42)
# print(ws.average_rating)    # 4.4
# print(ws.count_of_ratings)  # 42
# ws.rate_service(4)
# print(ws.average_rating)    # 4.4
# print(ws.count_of_ratings)  # 43
