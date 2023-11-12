from system_interface.system_interface import SystemInterface
from vehicle.vehicles import InvalidVinError
from cost.vehicle_costs import DAILY_RENTAL, WEEKLY_RENTAL, WEEKEND_RENTAL
from reservation.reservation import Reservation


class RentalAgencyUI:
    """This class provides a console interface for the rental agency system."""

    def __init__(self, sys):
        """Stores the provided reference to the vehicle rental systems."""
        self.__sys = sys

    def start(self):
        """Begins the command loop."""
        self.__displayWelcomeScreen()
        self.__displayMenu()

        selection = self.__getSelection(7)

        while selection != 7:
            self.__executeCmd(selection)
            self.__displayMenu()
            selection = self.__getSelection(7)

        print("Thank you for using the Friendly Rental Agency!")

    # private menthods
    def __displayWelcomeScreen(self):
        """PRIVATE: Displays welcome message and general instructions."""
        print("******************************************************")
        print("****Welcome To The Friendly Vehicle Reantal Agency****")
        print("******************************************************")

    def __displayMenu(self):
        """PRIVATE: Display a list of menu options on the screen."""
        print("\n<<< MAIN MENU >>>")
        print("1 - Display vehicle types")
        print("2 - Check rental costs")
        print("3 - Check available vehicles")
        print("4 - Get cost of  specific rental")
        print("5 - Make a reservation")
        print("6 - Cancel a reservation")
        print("7 - Quit\n")

    def __getSelection(self, num_selections, promt="Enter: ") -> str:
        """PRIVATE: Returns user-entered value in range 1 - num_selections."""
        valid_input = False
        selection = input(promt)

        while not valid_input:
            try:
                selection = int(selection)

                if selection < 1 or selection > num_selections:
                    print("* Invalid Entry *\n")
                else:
                    valid_input = True

            except ValueError:
                selection = input(promt)

        return selection
