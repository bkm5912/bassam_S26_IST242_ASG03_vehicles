"""
Control and logic of the program
"""
from manufacturer import Manufacturer
from auto_model import AutoModel
from sedan import Sedan
def main():
    s = Sedan(
        Manufacturer("Honda", "Japan"),
            AutoModel("Civic", False, []),
            28
    )
    print(s.how_far_with(10))



if __name__ == "__main__":
    main()