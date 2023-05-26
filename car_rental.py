class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


class Car(Vehicle):
    def __init__(self, brand, model, year, rental_rate, is_available=True):
        super().__init__(brand, model, year)
        self.rental_rate = rental_rate
        self.is_available = is_available

    def rent(self, customer):
        try:
            if self.is_available:
                self.is_available = False
                print(f"The {self.brand} {self.model} is rented by {customer}.")
            else:
                raise Exception(f"The {self.brand} {self.model} is not available for rent.")
        except Exception as e:
            print("An error occurred:", str(e))

    def return_car(self, days_rented):
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
        return self.rental_rate * days_rented


class RentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def display_available_cars(self):
        try:
            available_cars = [car for car in self.cars if car.is_available]
            print("Available cars:")
            for car in available_cars:
                print(f"{car.brand} {car.model} ({car.year})")
        except Exception as e:
            print("An error occurred:", str(e))

    def rent_car(self, car_index, customer):
        try:
            if car_index < len(self.cars):
                car = self.cars[car_index]
                car.rent(customer)
            else:
                raise Exception("Invalid car index.")
        except Exception as e:
            print("An error occurred:", str(e))

    def return_car(self, car_index, days_rented):
        try:
            if car_index < len(self.cars):
                car = self.cars[car_index]
                car.return_car(days_rented)
            else:
                raise Exception("Invalid car index.")
        except Exception as e:
            print("An error occurred:", str(e))
