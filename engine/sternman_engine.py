from abc import ABC
from engine.engine import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_on: book):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return self.warning_light_on
