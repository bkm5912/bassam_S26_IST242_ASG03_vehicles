'''
Years the models are produced
'''

class AutoModel:
    """
    creates automodel class
    """
    def __init__(self, name : str, in_production : bool, years : list[int]):
        if not years:
            raise ValueError("years list cannot be empty")
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
    
    @property
    def first_year(self):
        """
        Returns the first year it was produced
        """
        return self._years[0]
    
    def __str__(self):
        return f"{self._name} in production = {self._in_production},  release year: {self._years[0]}"