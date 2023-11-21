from prac_09.unreliable_car import UnreliableCar


def main():
    """Demo test code to show how to use car class."""
    my_car = UnreliableCar("Haotian", 100, 50)
    my_car.drive(10)
    print(my_car)


main()