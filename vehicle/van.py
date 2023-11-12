from vehicle.vehicle import Vehicle

class Van(Vehicle):
    """This class is a subtype of the Vehicle class"""
    def __init__(self, make_model: str, mpg: str, num_passengers: str, vin: str):
        """Initialized with provided parameter values."""
        super().__init__(mpg, vin)

        self.__make_model = make_model
        self.__num_passengers = num_passengers

    def getDescription(self) -> str:
        """Returns description of car as formatted string"""
        return f'{self.__make_model}  passengers:{self.__num_passengers}  {super().getDescription()}'
