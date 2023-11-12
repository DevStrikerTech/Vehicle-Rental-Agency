"""
This program performs the task of a vehicle rental agency, including the
display of vehicle information and the ability to make/cancel reservations.
"""
from system_interface.system_interface import SystemInterface
from rental_agency_ui.rental_agency_ui import RentalAgencyUI

try:
    # create system with populated data from files
    sys = SystemInterface()

    # associate user interface with system
    ui = RentalAgencyUI(sys)

    # start the user interfae
    ui.start()

except IOError:
    print("** PROGRAM TERMINATION (IO Error) **")
