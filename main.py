from car_rental import Car, RentalSystem

def main():
    # Create a rental system
    rental_system = RentalSystem()

    # Create and add cars to the rental system
    car1 = Car("Toyota", "Camry", 2020, 50.0)
    car2 = Car("Honda", "Accord", 2019, 60.0)
    car3 = Car("Ford", "Mustang", 2021, 80.0)
    rental_system.add_car(car1)
    rental_system.add_car(car2)
    rental_system.add_car(car3)

    # Display available cars
    rental_system.display_available_cars()

    # Rent a car
    car_index = int(input("Enter the car index to rent: "))
    customer = input("Enter customer name: ")
    rental_system.rent_car(car_index, customer)

    # Return a car
    car_index = int(input("Enter the car index to return: "))
    days_rented = int(input("Enter the number of days rented: "))
    rental_system.return_car(car_index, days_rented)

if __name__ == "__main__":
    main()
