from datetime import timedelta
import math


class Auto():
    def __init__(self, color="black", model="BMW", type_of_drive="automotive", mileage=30, price_new=10000000, price_now=8000000, gps_now=[201, 20], max_speed=220, type_engine="petrol", fuel_consumption=0.2, petrol_now=60, interval_service=timedelta(days=180)):
        self.color = color
        self.model = model
        self.type_of_drive = type_of_drive
        self.mileage = mileage
        self.price_new = price_new
        self.price_now = price_now
        self.gps_now = gps_now
        self.max_speed = max_speed
        self.type_engine = type_engine
        self.fuel_consumption = fuel_consumption
        self.petrol_now = petrol_now
        self.interval_service = interval_service

    def go_to_city(self, gps):
        distance = self.distance_to_gps_point(gps)
        return self.petrol_now / self.fuel_consumption >= distance

    def distance_to_gps_point(self, target_gps):
        lat1, lon1 = math.radians(self.gps_now[0]), math.radians(self.gps_now[1])
        lat2, lon2 = math.radians(target_gps[0]), math.radians(target_gps[1])
        distance = 6371 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1))
        return distance


    def trip_cost(self, gps, fuel_cost):
        distance = self.distance_to_gps_point(gps)
        litr_need = distance * self.fuel_consumption
        res_cost = litr_need * fuel_cost
        return res_cost

    def time_trip(self, gps):
        return self.distance_to_gps_point(gps) / self.max_speed

    def price_loss(self):
        return self.price_new - self.price_now