# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
temp_input = input("Enter the temperature value: ")
unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

# Validate input and perform conversion
try:
    temp_value = float(temp_input)  # check if numeric
    if unit == 'C':
        converted = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted:.2f}°F")
    elif unit == 'F':
        converted = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
