class Car:
    def __init__(self, colour, model, year):
        self.colour = colour
        self.model = model
        self.year = year
        self.fuel_level = 100
        self.engine_on = False

    def start_engine(self):
        if self.engine_on:
            print("Engine is already on")
        else:
            if self.fuel_level > 0:
                self.engine_on = True
                print("Engine Started")
            else:
                print("No fuel")

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            print("Engine stopped")
        else:
            print("Engine is already off")

    def refuel(self, amount):
        self.fuel_level += amount
        print(f"Refuelling with {amount} litres of fuel.")

    def drive(self, distance):
        distance_cover = 10*self.fuel_level
        if distance_cover >= distance and self.engine_on:
            print(f"Driving {distance} km.")
            self.fuel_level -= distance/10
        else:
            print("Insufficient fuel or engine is off")

    def display_info(self):
        print(f"{self.year} {self.colour} {self.model} | Fuel Level: {self.fuel_level} | Engine: {self.engine_on}")


if __name__ == "__main__":
    # Creating an instance of car.
    my_car = Car("Silver", "BMW", 2023)

    # Invoking instance methods.
    my_car.start_engine()
    my_car.drive(800)
    my_car.drive(300)
    my_car.refuel(10)
    my_car.drive(300)
    my_car.stop_engine()

    # Displaying updated information.
    my_car.display_info()

