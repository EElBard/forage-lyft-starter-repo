from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        service = False
        for tire in self.tire_array:
            if tire > 0.9:
                service = True
        return service
