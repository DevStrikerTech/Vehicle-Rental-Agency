class Vehicle:
    """The Vehicle class holds the mpg, vin and ereserved flag of a vehicle."""
    def __init__(self, mpg: str, vin: str):
        """Intializes a Vehicle objext with mpg and vin."""
        self.__mpg = mpg
        self.__vin = vin
        self.__reserved = False

    def getType(self) -> str:
        """Returns the type of vehicle."""
        return  type(self).__name__
    
    def getVin(self) -> str:
        """Returns the vin of vehicle."""
        return self.__vin
    
    def getDescription(self) -> str:
        """Returns general description of car, not specific to type."""
        return f'mpg:{self.__mpg}  vin:{self.__vin}'
    
    def isReserved(self) -> bool:
        """Returns True if vehicle is reserved, otherwise returns False"""
        return self.__reserved
    
    def setReserved(self, reserved):
        """Sets reserved flag of vehicle to provided Boolean value"""
        self.__reserved = reserved
