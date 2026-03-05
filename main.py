"""
Control and logic of the program
"""
from manufacturer import Manufacturer
from auto_model import AutoModel
from sedan import Sedan
from truck import Truck
from garage import Garage
def main():

    # Trucks
    f150 = Truck(Manufacturer("Ford", "USA"),
                 AutoModel("F150", True, list[range(2020, 2022)], 20.0)
                 )
    tundra = Truck(Manufacturer("Toyota", "Japan"),
                 AutoModel("Tundra", False, list[range(1987, 1988)], 30.0, is_dually = True)
                 )

    # Sedans
    s = Sedan(
        Manufacturer("Honda", "Japan"),
            AutoModel("Civic", False, []),
            28
    )

    civic = Sedan(
        Manufacturer("Honda", "Japan"),
            AutoModel("Civic", False, list[range(1990, 1998)]),
            28
    )

    m3 = a
    print(s.how_far_with(10))

    g = Garage()
    g.add_vehicle(f150)
    g.add_vehicle(civic)
    g.add_vehicle(m3)
    g.add_vehicle(tundra)



if __name__ == "__main__":
    main()