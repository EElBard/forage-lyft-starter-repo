from abc import ABC, abstractmethod

from battery.battery import Battery
from engine.engine import Engine
from serviceable import Serviceable


class Car(Serviceable, ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self) -> bool:
        pass
