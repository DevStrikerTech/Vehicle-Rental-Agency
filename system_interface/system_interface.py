from vehicle.vehicles import Vehicles
from vehicle.car import Car
from vehicle.van import Van
from vehicle.truck import Truck
from cost.vehicle_cost import VehicleCost
from cost.vehicle_costs import VehicleCosts
from reservation.reservations import Reservations


# symbolic constants
VEHICLE_TYPES = ('Car', 'Van', 'Truck')
VEHICLES_FILENAME = 'vehicles_stock.txt'
VEHICLE_COSTS_FILENAME = 'rental_costs.txt'

# exception class
class InvalidFileFormatError(Exception):
    """Exception indicationg invalid file in file_name."""

    def __init__(self, header, file_name):
        self.__header = header
        self.__file_name = file_name

    def __str__(self) -> str:
        return f'FILE FORMAT ERROR: file header {self.__header} exception is file {self.__file_name}'
    
class SystemInterface:
    """This class provides the system interface of the vehicle rental system."""