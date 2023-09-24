def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    choice = input("Choose Celsius(C) to Fahrenheit or Fahrenheit(F) to Celsius? (C/F): ").upper()

    if choice not in ["C", "F"]:
        print("Invalid choice. Please enter 'C' or 'F'.")
        return

    try:
        temp = float(input("Enter temperature: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice == "C":
        print(f"{temp} Celsius is {celsius_to_fahrenheit(temp)} Fahrenheit.")
    else:
        print(f"{temp} Fahrenheit is {fahrenheit_to_celsius(temp)} Celsius.")

convert_temperature()
