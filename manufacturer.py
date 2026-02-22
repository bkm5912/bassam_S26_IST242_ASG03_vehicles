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
    
    @property
    def get_country(self):
        """
        Returns the manufacturer's country
        """
        return self._country
    
    def __str__(self):
        """
        Prints the manufacturer object (name and country)
        """
        return f"({self._name}, {self._country})"