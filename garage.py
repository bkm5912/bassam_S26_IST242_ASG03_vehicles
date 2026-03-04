from vehicle import Vehicle

"""
This is a private list of vehicles
"""

class Garage:
    # Create the constructor
    def __init__(self):
        self._vehicles: list[Vehicle] = []

    # Create the getter
    @property
    def vehicles(self) -> list[Vehicle]:
        return list[self._vehicles]

    def add_vehicle(self, vehicles: Vehicle) -> None:
        """
        Add a vehicle to the list
        """
        self._vehicles.append(Vehicle)

    def empty_garage(self):
        """
        Empty the garage of all the vehicles
        """
        self._vehicles.clear()