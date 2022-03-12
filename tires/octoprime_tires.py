from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        total = 0
        for tire in self.tire_array:
            total += tire
        if total >= 3:
            return True
        return False
