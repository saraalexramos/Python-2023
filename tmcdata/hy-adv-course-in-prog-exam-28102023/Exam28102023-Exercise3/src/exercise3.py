class Driver:
    def __init__(self, name: str, year_of_birth: int,
            height: int, weight: int):
        self.name = name
        self.year_of_birth = year_of_birth
        self.height = height
        self.weight = weight

    def __str__(self):
        return (f"Driver(name = {self.name}, " +
            f"year_of_birth = {self.year_of_birth}, " +
            f"height = {self.height}, weight = {self.weight})")

class RallyCar:
    def __init__(self, make: str, top_speed: int, driver: Driver):
        self.make = make
        self.top_speed = top_speed
        self.driver = driver

    def __str__(self):
        return (f"RallyCar(make = {self.make}, " +
            f"top_speed = {self.top_speed}, " +
            f"driver = {self.driver})")
    

def fastest_cars (cars:list, speed: int):
    makes = []
    for car in cars:
        if car.top_speed > speed:
            makes.append(car.make)
    return makes

def drivers_of_make(cars: list, make: str):
    drivers = []
    for car in cars:
        if car.make == make:
            drivers.append(car.driver)
    return drivers

def youngest_and_oldest_driver(drivers: list):
    youngest_age = 0
    oldest_age = 2023
    youngest = ""
    oldest = ""
    for driver in drivers:
        if driver.year_of_birth > youngest_age:
            print(driver)
            print("year", driver.year_of_birth)
            print("youngest", youngest_age)

            youngest = driver.name
            youngest_age = driver.year_of_birth
        elif driver.year_of_birth < oldest_age:
            oldest = driver.name
            oldest_age = driver.year_of_birth
    return (youngest, oldest)

def by_speed(cars: list):
    cars_by_speed = sorted(cars, key = lambda x: x.top_speed, reverse = True)
    return cars_by_speed



if __name__ == "__main__":
    john = Driver("John", 1996, 170, 80)
    mercedes1 = RallyCar("mercedes1", 230, john)
    mercedes2 = RallyCar("mercedes2", 190, john)
    mercedes3 = RallyCar("mercedes3", 220, john)
    audi1 = RallyCar("audi1", 210, john)
    audi2 = RallyCar("audi2", 180, john)
    audi3 = RallyCar("audi3", 197, john)
    cars = [mercedes1, mercedes2, mercedes3, audi1, audi2, audi3]
    print(fastest_cars(cars, 200))

    dinis = Driver("Dinis", 2000, 170, 80)
    arthur = Driver("Arthur", 1989, 170, 80)
    william = Driver("William", 1988, 170, 80)
    kyle = Driver("Kyle", 1967, 170, 80)
    drivers = [john, dinis, arthur, william, kyle]
    print(youngest_and_oldest_driver(drivers))
    x = by_speed(cars)
    for y in x :
        print(y.make)