from vehicle.vehicle import Vehicle

class Car(Vehicle):
    """This class is a subtype of the Vehicle class"""
    def __init__(self, make_model: str, mpg: str, num_passengers: str, num_doors: str, vin: str):
        """Initialized with provided parameter values."""
        super().__init__(mpg, vin)

        self.__make_model = make_model
        self.__num_passengers = num_passengers
        self.__num_doors= num_doors

    def getDescription(self) -> str:
        """Returns description of car as formatted string"""
        return f'{self.__make_model}  passengers:{self.__num_passengers}  doors:{self.__num_doors}  {super().getDescription()}'
