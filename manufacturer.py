class Manufacturer:
    '''
    Docstring for Manufacturer
    '''
    # constructor
    def __init__(self, name: str, country: str):
        self.__name = name
        self.__country = country

    # getter functions
    @property
    def get_name(self) -> str:
        return self.__name
    
    @property
    def get_country(self) -> str:
        return self.__country


