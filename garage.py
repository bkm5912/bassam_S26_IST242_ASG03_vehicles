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
        return list(self._vehicles)

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """
        Add a vehicle to the list
        """
        self._vehicles.append(vehicle)

    def empty_garage(self):
        """
        Empty the garage of all the vehicles
        """
        self._vehicles.clear()

    def sort_by_release_year(self):
        self._vehicles.sort()

    def __str__(self) -> str:
        return "\n".join(str(v) for v in self._vehicles)