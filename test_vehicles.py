"""
Unit testing file
Tester: Bassam Mamari

Use pytest -v to test
"""

import pytest


from manufacturer import Manufacturer

class TestManufacturer:
    def test_constructor(self):
        m = Manufacturer("Ford", "USA")
        assert m.get_name == "Ford"
        assert m.get_country == "USA"

    def test_constructor_2(self):
        m = Manufacturer("Honda", "Japan")
        assert m.get_name == "Honda"
        assert m.get_country == "Japan"

    def test_str(self):
        m = Manufacturer("BMW", "Germany")
        assert str(m) == "(BMW, Germany)"