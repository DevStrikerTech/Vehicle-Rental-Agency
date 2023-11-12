from vehicle.vehicle import Vehicle
from vehicle.car import Car
from vehicle.van import Van
from vehicle.truck import Truck
from vehicle.vehicles import Vehicles

def test_vehicle():
    veh = Vehicle('32', 'ABC123')
    assert veh.getType() == 'Vehicle'
    assert veh.getVin() == 'ABC123'

def test_car():
    veh = Car('Ford Fusion', '34', '5', '4', 'AB4FG5689MG')
    assert veh.getDescription() == 'Ford Fusion  passengers:5  doors:4  mpg:34  vin:AB4FG5689MG'

def test_van():
    veh = Van('Dodge Caravan', '25', '7', 'TF1000')
    assert veh.getDescription() == 'Dodge Caravan  passengers:7  mpg:25  vin:TF1000'

def test_truck():
    veh = Truck('12', '10', '1', 'HG1000')
    assert veh.getDescription() == 'length(feet):10  rooms:1  mpg:12  vin:HG1000'

def test_vehicles():
    car = Car('Ford Fusion', '34', '5', '4', 'FG1000')
    veh = Vehicles()
    veh.addVehicle(car)
    assert veh.getAvailVehicles('Car')[0].getDescription() == 'Ford Fusion  passengers:5  doors:4  mpg:34  vin:FG1000'
