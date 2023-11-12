from vehicle.vehicle import Vehicle

class Truck(Vehicle):
    """This class is a subtype of the Vehicle class"""
    def __init__(self, mpg: str, length: str, num_rooms: str, vin: str):
        """Initialized with provided parameter values."""
        super().__init__(mpg, vin)

        self.__length = length
        self.__num_rooms = num_rooms

    def getDescription(self) -> str:
        """Returns description of car as formatted string"""
        return f'length(feet):{self.__length}  rooms:{self.__num_rooms}  {super().getDescription()}'
