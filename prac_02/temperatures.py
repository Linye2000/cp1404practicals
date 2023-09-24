def convert_temperature(choice, temp):
    return (temp * 9/5) + 32 if choice == "C" else (temp - 32) * 5/9

choice = input("Convert from Celsius(C) to Fahrenheit or Fahrenheit(F) to Celsius? (C/F): ").upper()
temp = float(input("Enter temperature: "))

converted_temp = convert_temperature(choice, temp)

if choice == "C":
    print(f"{temp} Celsius is {converted_temp} Fahrenheit.")
elif choice == "F":
    print(f"{temp} Fahrenheit is {converted_temp} Celsius.")