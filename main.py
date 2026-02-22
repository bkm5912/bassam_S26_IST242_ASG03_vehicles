"""
Control and logic of the program
"""
from manufacturer import Manufacturer
from auto_model import AutoModel
def main():
    """
    Main function, control the rest of the program/call functions
    """
    m = Manufacturer("Ford", "USA")
    print(m.get_name)
    print(m.get_country)
    print(m)

    original_list = [2020, 2021]
    am = AutoModel("F150", True, original_list)
    print(am.get_years)
    original_list.clear
    print(am.get_years)