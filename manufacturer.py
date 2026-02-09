class Manufacturer:
    '''
    Docstring for Manufacturer
    '''
    # constructor
    def __init__(self, name: str, country: str):
        self._name = name
        self._country = country


    # properties
    @property
    def name(self) -> str:
        return self._name