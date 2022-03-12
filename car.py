from abc import ABC, abstractmethod

from battery.battery import Battery
from engine.engine import Engine
from serviceable import Serviceable
from tires.tires import Tires


class Car(Serviceable, ABC):
    def __init__(self, engine: Engine, battery: Battery, tires: Tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
