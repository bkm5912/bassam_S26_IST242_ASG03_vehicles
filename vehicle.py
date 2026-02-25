from abc import ABC, abstractmethod
# from functools import total_ordering # sorting purposes

from manufacturer import Manufacturer
from auto_model import AutoModel

class Vehicle(ABC):
    """
    Abstract base class (ABC) for all vehicles
    """
    # Constructor
    def __init__(self, 
                 manufacturer: Manufacturer,
                 model: AutoModel,
                 mpg: float):
        self._manufacturer = manufacturer
        self._model = model
        self._mpg = mpg


    # Getters
    @property
    def manufacturer(self) -> Manufacturer:
        return self._manufacturer

    @property
    def model(self) -> AutoModel:
        return self._model
    
    @property
    def mpg(self) -> float:
        return self._mpg