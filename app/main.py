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
            if car.clean_mark < self.clean_power:
                dif_clean = self.clean_power - car.clean_mark
                rating_distance = self.average_rating / self.distance_from_city_center
                income_car = car.comfort_class * dif_clean * rating_distance
                income += income_car
                car.clean_mark = self.clean_power
        income = Decimal(income)
        return income.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        # return round(income, 1)


    def calculate_washing_price(self, car):
        dif_clean = self.clean_power - car.clean_mark
        rating_distance = self.average_rating / self.distance_from_city_center
        income_car = car.comfort_class * dif_clean * rating_distance
        # income_car = Decimal(income_car)
        # return income_car.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        return round(income_car, 1)


    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power


    def rate_service(self, rate):
        old_rates = self.average_rating * self.count_of_ratings
        new_count = self.count_of_ratings + 1
        new_rates = (old_rates + rate) / new_count
        new_rates = Decimal(new_rates)
        self.average_rating = new_rates.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        self.count_of_ratings = new_count
        return new_rates.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        # return round(new_rates, 1)

