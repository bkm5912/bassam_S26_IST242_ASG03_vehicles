class Manufacturer:
    '''
    Creates manufacturer class
    '''
    # Constructor
    def __init__(self, name: str, country: str):
        # Name of manufacturer
        self._name = name
        # Name of manufacturer's country
        self._country = country

    # Getters (properties)
    @property
    def get_name(self):
        """
        Returns the name
        """
        return self._name