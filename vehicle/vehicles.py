class InvalidVinError(Exception):
    """Exception indicating that a provided vin was not found."""
    pass

class Vehicles:
    """This class maintains a collection of Vehicle objects."""
    def __init__(self):
        """Initializes empty list of vehicles."""
        self.__vehicles = []

    def getVehicle(self, vin: str) -> str:
        """Returns Vehicle for provided vin. Raises InvalidVinError."""
        for vehicle in self.__vehicles:
            if vehicle.getVin() == vin:
                return vehicle
            
        raise InvalidVinError
    
    def addVehicle(self, vehicle: str):
        """Adds new vehicle to list of vehicles."""
        self.__vehicles.append(vehicle)

    def numAvailVehicles(self, vehicle_type: str):
        """Returns a list of unreserved Vehicles objects of vehicle_type."""
        return len(self.getAvailVehicles(vehicle_type))
    
    def getAvailVehicles(self, vehicle_type: str) -> list:
        """Returns a list of unreserved Vehicles objects of vehicle_type."""
        return [vehicle for vehicle in self.__vehicles if vehicle.getType() == vehicle_type and not vehicle.isReserved()]
    
    def unreserveVehicle(self, vin):
        """Sets reservation status of vehicle with vin to unreserved."""
        key = 0
        found = False

        while not found:
            if self.__vehicles[key].getVin() == vin:
                self.__vehicles[key].setReserved(False)
                found = True
