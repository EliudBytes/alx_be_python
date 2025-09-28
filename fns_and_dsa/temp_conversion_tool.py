# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # Prompt for temperature and validate numeric input (raise ValueError if invalid)
    temp_str = input("Enter the temperature to convert: ")
    try:
        temperature = float(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt for unit (accept 'C', 'celsius', 'F', 'fahrenheit')
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if unit in ("c", "celsius"):
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    elif unit in ("f", "fahrenheit"):
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()


