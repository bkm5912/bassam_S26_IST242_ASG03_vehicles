'''
Years the models are produced
'''

class AutoModel:
    """
    creates automodel class
    """
    def __init__(self, name : str, in_production : bool, years : list[int]):
        # Name of automodel
        self._name = name
        # If it's still in production
        self._in_production = in_production
        # Years of production
        self._years = list(years)

    # Properties
    @property
    def name(self):
        """
        Returns the name
        """
        return self._name
    
    @property
    def in_production(self):
        """
        Returns if it's still in production
        """
        return self._in_production
    
    @property
    def years(self):
        """
        Returns the years of production
        """
        return list(self._years)
    
    def __str__(self):
        return f"{self._name} inproduction = {self._in_production}"
        f"  release years = {self._years}"