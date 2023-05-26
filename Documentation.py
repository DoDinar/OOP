class Vehicle:
    """
    Class representing a vehicle.

    Attributes:
        - brand (str): The brand of the vehicle.
        - model (str): The model of the vehicle.
        - year (int): The year of manufacture of the vehicle.
    """

    def __init__(self, brand, model, year):
        """
        Initializes a new instance of the Vehicle class.

        Parameters:
            - brand (str): The brand of the vehicle.
            - model (str): The model of the vehicle.
            - year (int): The year of manufacture of the vehicle.
        """
        self.brand = brand
        self.model = model
        self.year = year


class Car(Vehicle):
    """
    Class representing a car.

    Attributes:
        - rental_rate (float): The rental rate of the car per day.
        - is_available (bool): Flag indicating if the car is available for rent.
    """

    def __init__(self, brand, model, year, rental_rate, is_available=True):
        """
        Initializes a new instance of the Car class.

        Parameters:
            - brand (str): The brand of the car.
            - model (str): The model of the car.
            - year (int): The year of manufacture of the car.
            - rental_rate (float): The rental rate of the car per day.
            - is_available (bool, optional): Flag indicating if the car is available for rent (default True).
        """
        super().__init__(brand, model, year)
        self.rental_rate = rental_rate
        self.is_available = is_available

    def rent(self, customer):
        """
        Rents the car to a customer.

        Parameters:
            - customer (str): The name of the customer renting the car.
        """
        try:
            if self.is_available:
                self.is_available = False
                print(f"The {self.brand} {self.model} is rented by {customer}.")
            else:
                raise Exception(f"The {self.brand} {self.model} is not available for rent.")
        except Exception as e:
            print("An error occurred:", str(e))

    def return_car(self, days_rented):
        """
        Returns the car after rental.

        Parameters:
            - days_rented (int): The number of days the car was rented for.
        """
        try:
            if not self.is_available:
                self.is_available = True
                rental_cost = self.calculate_rental_cost(days_rented)
                print(f"The {self.brand} {self.model} has been returned. Rental cost: {rental_cost}")
            else:
                raise Exception(f"The {self.brand} {self.model} was not rented.")
        except Exception as e:
            print("An error occurred:", str(e))

    def calculate_rental_cost(self, days_rented):
        """
        Calculates the rental cost of the car.

        Parameters:
            - days_rented (int): The number of days the car was rented for.

        Returns:
            - float: The rental cost of the car.
        """
        return self.rental_rate * days_rented


class RentalSystem:
    """
    Class representing a car rental system.

    Attributes:
        - cars (list): List of cars in the rental system.
    """

    def __init__(self):
        """Initializes a new instance of the RentalSystem class."""
        self.cars = []

    def add_car(self, car):
        """
        Adds a car to the rental system.

        Parameters:
            - car (Car): The car to be added to the system.
        """
        self.cars.append(car)

    def display_available_cars(self):
        """Displays the available cars for rent."""
        try:
            available_cars = [car for car in self.cars if car.is_available]
            print("Available cars:")
            for car in available_cars:
                print(f"{car.brand} {car.model} ({car.year})")
        except Exception as e:
            print("An error occurred:", str(e))

    def rent_car(self, car_index, customer):
        """
        Rents a car by index.

        Parameters:
            - car_index (int): The index of the car in the list.
            - customer (str): The name of the customer renting the car.
        """
        try:
            if car_index < len(self.cars):
                car = self.cars[car_index]
                car.rent(customer)
            else:
                raise Exception("Invalid car index.")
        except Exception as e:
            print("An error occurred:", str(e))

    def return_car(self, car_index, days_rented):
        """
        Returns a car after rental by index.

        Parameters:
            - car_index (int): The index of the car in the list.
            - days_rented (int): The number of days the car was rented for.
        """
        try:
            if car_index < len(self.cars):
                car = self.cars[car_index]
                car.return_car(days_rented)
            else:
                raise Exception("Invalid car index.")
        except Exception as e:
            print("An error occurred:", str(e))
