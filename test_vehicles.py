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