from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel

class Truck(Vehicle):
    """
    Represents a sedan type of vehicle
    """
    
    # Create a constructor
    def __init__(self, 
                 manufacturer: Manufacturer,
                 model: AutoModel,
                 mpg: float,
                 # Additional attribute for truck
                 is_dually: bool = False):
        super().__init__(manufacturer, model, mpg)
        self._is_dually = is_dually

    
    # Specify the abstract method
    def number_of_wheels(self) -> int:
        return 6 if self._is_dually else 4
    
    # Create release year getter
    @property
    def release_year(self):
        return self.model.first_year
    
    # Create is dually getter
    @property
    def is_dually(self) -> bool:
        return self._is_dually
    
    # Printing sedan
    def __str__(self) -> str:
        return (
            f"({self._manufacturer}) {self._model}, mpg: {self._mpg:.2f}"
            f" is dually truck: {self._is_dually}"
        )