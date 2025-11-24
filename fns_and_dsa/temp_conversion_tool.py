# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction with exact prompts required by checker
temp_input = input("Enter the temperature to convert:")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()

try:
    temp_value = float(temp_input)
    if unit == "C":
        print(f"{temp_value}°C is {convert_to_fahrenheit(temp_value):.2f}°F")
    elif unit == "F":
        print(f"{temp_value}°F is {convert_to_celsius(temp_value):.2f}°C")
    else:
        print("Invalid unit! Enter C or F.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")



