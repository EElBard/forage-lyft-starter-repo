from datetime import date
from abc import ABC
from battery.battery import Battery


class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return self.last_service_date < self.current_date.replace(year = self.current_date.year - 3)
